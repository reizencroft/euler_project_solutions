# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

limit = 2000000
sum = 0

for i in range(2, limit+1):
    # print("%d, %s" % (i, is_prime(i)))
    if is_prime(i):
        sum += i

print(sum)