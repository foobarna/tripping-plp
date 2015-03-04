from math import sqrt
from timeit import default_timer as timer
import time


def time_measure(func):
    """Decorator for measuring the execution time in seconds of a function."""
    def measure(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        print "Execution of %s took %s s." % (func.__name__, end - start)
        return result

    return measure


def total_time_measure(func, total=[0]):
    """Decorator for measuring the execution time in seconds of all functions decorated by it."""
    def measure(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        total[0] += end - start
        print "Execution so far: %s." % total[0]
        return result

    return measure



def check_prime(n):
    """Checks if a number is prime and return true if so, false otherwise."""
    if n <= 1:
        return False

    is_prime = True
    n_root = int(sqrt(n)) + 1
    for i in xrange(2, n_root):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


def primes_range(stop):
    """Returns a list of prime numbers starting from 2 and lower than limit."""
    return [i for i in range(2, stop) if check_prime(i)]


def fibonacci_iterative(n):
    """Returns a list of n fibonacci natural numbers calculated iteratively."""
    a = -1
    b = 1
    fibs = list()
    for i in range(n):
        c = a + b
        fibs.append(c)
        a, b = b, c

    return fibs


def fibonacci_recursive(n):
    """Returns a list of n fibonacci natural numbers calculated recursively."""
    if n < 1:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [0, 1]
    else:
        fibs = fibonacci_recursive(n-1)
        prevs = fibs[-2:]
        fibs.append(prevs[0] + prevs[1])
        return fibs


def my_map(func, sequence):
    """Returns a list after applying the function to each item of sequence."""
    return [func(item) for item in sequence]


def my_filter(func, sequence):
    """Returns a list after applying the filter to each item of sequence."""
    return [item for item in sequence if func(item)]


def my_reduce(func, iterable, initializer=None):
    """
    Applies the function to prev element (or initializer for the first time) from left to right using the previous value
     as the first parameter of the function. Return the final result.
    """
    items = iter(iterable)

    if initializer is None:
        initializer = next(items)

    prev = initializer
    for i in items:
        prev = func(prev, i)

    return prev


def sum_fancy_numbers(stop):
    """Sums up all the numbers n that are lower than the input and have the property 3 | n * n - 1."""
    return my_reduce(lambda a, b: a+b, my_filter(lambda x: True if (x * x - 1) % 3 == 0 and x > 2 else False, range(1, stop)))


@total_time_measure
@time_measure
def bubble_sort(sequence):
    """Performs sorting for the list using bubble sort algorithm."""
    time.sleep(1.2)
    for i in xrange(len(sequence)):
        modified = False
        for k in xrange(len(sequence) - 1, i, -1):
            if sequence[k] < sequence[k - 1]:
                sequence[k], sequence[k - 1] = sequence[k - 1], sequence[k]
                modified = True

        if not modified:
            break

@total_time_measure
@time_measure
def binary_search(sequence, value):
    """Searches for a value in a sorted list in a divide et impera manner, returns True if found and false otherwise"""
    time.sleep(2.3)
    low, high = 0, len(sequence) - 1

    if sequence[low] > value or value > sequence[high]:
        return False

    while low != high:
        mid = (low + high) / 2
        if value == sequence[mid]:
            return True
        elif value > sequence[mid]:
            low = mid
        else:
            high = mid

    return False


def foo(bar=[0]):
    """Every time it's called it returns an incremented value by 1 from previous call, starting from 0. """
    bar[0] += 1
    return bar[0]


if __name__ == "__main__":
    # num = int(raw_input("Number: "))
    # result = "is prime" if check_prime(num) else "is not prime"
    # print result
    #
    # upper_limit = int(raw_input("Upper limit: "))
    # primes = ", ".join(map(str, primes_range(upper_limit)))
    # print primes
    #
    # fib_no = int(raw_input("Fibonacci numbers: "))
    # print "iterative: ", fibonacci_iterative(fib_no)
    # print "recursive: ", fibonacci_recursive(fib_no)
    #
    # print my_map(str.upper, ["test", "test1", "test2"])
    # print my_filter("test".__eq__, ["test", "test1", "test2"])
    # print my_reduce(lambda a, b: a+b, [1, 1, 1, 1])
    #
    # print sum_fancy_numbers(5)
    #
    sortable_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    bubble_sort(sortable_list)
    print "Bubble sort: ", sortable_list
    searched_value = 7
    print "Search for %s: %s" % (searched_value, binary_search(sortable_list, searched_value))
    #
    # print "stateful function returns: ", foo(), foo(), foo()
