def reverse_input_name():
    """Read a name and print its reverse."""
    name = raw_input("Name: ")
    reversed_name = name[::-1]
    print "Your reverse name is: ", reversed_name


def check_number_palindrome():
    """Read a number and print if its palindrome or not."""
    num = int(raw_input("Number: "))
    n = num
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n /= 10

    result = "is" if num == reversed_num else "is not"
    print "%s a palindrome" % result


def palindromes():
    """Read a number and prints all lower palindromes."""
    n = int(raw_input("Give upper limit: "))

    pals = list()
    for i in range(0, n):
        i_str = str(i)
        if i < 10 or i_str == i_str[::-1]:
            pals.append(i_str)

    print ", ".join(pals)

if __name__ == '__main__':
    reverse_input_name()
    check_number_palindrome()
    palindromes()
