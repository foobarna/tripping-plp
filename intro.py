def intro1():
    name = raw_input("Name: ")
    reversed_name = name[::-1]
    print "Your reverse name is: ", reversed_name


def intro2():
    num = int(raw_input("Number: "))
    n = num
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n /= 10

    result = "is" if num == reversed_num else "is not"
    result += " a palindrome"
    print result


def intro3():
    n = int(raw_input("Give upper limit: "))

    for i in range(0, n):
        i_str = str(i)
        if i < 10 or i_str == i_str[::-1]:
            print i,

if __name__ == '__main__':
    intro1()
    intro2()
    intro3()
