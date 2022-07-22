PI = 3.14


def iseven(n):
    """
    Checks whether the given number is even number
    :param n: number to check
    :return:  True if number is even otherwise False
    """
    return n % 2 == 0


def ispositive(n):
    return n > 0


if __name__ == '__main__':  # running module directly
    print("Math Functions Ver 1.0")
    print(iseven(11), iseven(10), ispositive(10), ispositive(-10))
