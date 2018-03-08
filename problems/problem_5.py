def is_divisible_by_range(number, number_range):
    for i in number_range:
        if not number % i == 0:
            return False
    return True


if __name__ == "__main__":
    """ 2520 is the smallest number that can be divided by each of
    the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?"""
    value_range = range(2, 21)
    i = 2520
    while not is_divisible_by_range(i, value_range):
        i += 1
    print i

