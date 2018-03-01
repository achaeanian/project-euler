from math import sqrt


# Use primes as a sieve to reduce the amount of calculations required
shortcut_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def is_prime(x):
    i = 1
    root_x = sqrt(x)

    shortcuts = [
        prime for prime in shortcut_primes
        if prime < root_x
    ]
    for j in shortcuts:
        if x % j == 0 and j != 1 and j != x:
            return False

    while i < root_x:
        i += 1
        if i in shortcuts:
            continue
        if x % i == 0:
            return False

    shortcut_primes.append(x)
    return True

def largest_prime_factor_of_n(n):
    largest_prime_factor = 1
    i = 1
    root_n = sqrt(n)

    while i <= root_n:
        if n % i == 0 and is_prime(i):
            largest_prime_factor = i
        i += 1

    return largest_prime_factor


if __name__ == "__main__":
    """ The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?"""
    print largest_prime_factor_of_n(600851475143)

