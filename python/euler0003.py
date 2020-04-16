# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import sys

def is_prime(n):
    if n in primes:
        return True
    f = 2

    while f < n:
        if n % f == 0 and f != n:
            return False
        f += 1
    primes.append(n)
    return True

the_number = 600851475143
factor = 2
valid_factors = []
primes = [] 

while factor < the_number:
    if the_number % factor == 0:
        valid_factors.append(factor)
        y = the_number / factor
        valid_factors.append(int(y))
    factor += 1
    if factor in valid_factors:
        break

biggest = 0
for x in valid_factors:
    if is_prime(x) and x > biggest:
        biggest = x
        
print("Biggest %d" % biggest)