# https://projecteuler.net/problem=6
# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.


def sum_of_squares(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i**2
        i += 1
    return sum

def square_of_sum(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum**2

print(square_of_sum(100) - sum_of_squares(100))