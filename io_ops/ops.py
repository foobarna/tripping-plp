from fun import primes_range
import collections
import fileinput


def sum_numbers(filename):
    """Sums up all the numbers from a file, one number per line"""
    with open(filename, "r") as f:
        numbers = f.readlines()
        return reduce(lambda x, y: x+y, map(int, numbers))


def prime_numbers(filename):
    """Returns a list of prime numbers for each number in file's line."""
    with open(filename, "r") as f:
        numbers = f.readlines()
        return map(primes_range, map(int, numbers))


def unique_words(filename):
    """Checks the file for unique words and returns a list of them."""
    with open(filename, "r") as f:
        words = collections.Counter()
        map(words.update, map(str.split, f.readlines()))
        return [word for word, count in words.iteritems() if count == 1]


def merge_sorted(filenames, merged_filename="merged_sorted_numbers.out"):
    """Reads numbers from multiple files and outputs."""
    numbers_list = map(file.readlines, map(open, filenames))
    numbers = sorted([int(number) for sublist in numbers_list for number in sublist])
    with open(merged_filename, 'w') as fout:
        fout.writelines(map(lambda x: str(x) + '\n', numbers))


if __name__ == "__main__":
    # print sum_numbers("numbers.txt")
    # print prime_numbers("numbers.txt")
    # print unique_words("lorem.txt")
    merge_sorted(['numbers_sorted0.txt', 'numbers_sorted1.txt', 'numbers_sorted2.txt'])
