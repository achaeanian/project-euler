def is_palindrome(x):
    str_x = str(x)
    list_x = [digit for digit in str_x]
    r_list_x = list(reversed(list_x))
    return list_x == r_list_x


def biggest_palindrome_of_list(list_of_numbers):
    palindrome = 0

    for i in list_of_numbers:
        for j in list_of_numbers:
            z = i * j
            if z > palindrome:
                if is_palindrome(z):
                    palindrome = z
    return palindrome


if __name__ == "__main__":
    """ Find the largest palindromic number that is the product of two
    3 digit numbers.
    """

    values_to_trial = range(500, 1000)
    print biggest_palindrome_of_list(values_to_trial)

