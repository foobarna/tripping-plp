from math import sqrt


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


if __name__ == "__main__":
    num = int(raw_input("Number: "))
    result = "is prime" if check_prime(num) else "is not prime"
    print result

    upper_limit = int(raw_input("Upper limit: "))
    primes = ", ".join(map(str, primes_range(upper_limit)))
    print primes

    fib_no = int(raw_input("Fibonacci numbers: "))
    print fibonacci_iterative(fib_no)
    print fibonacci_recursive(fib_no)
