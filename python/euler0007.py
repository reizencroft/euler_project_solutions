# https://projecteuler.net/problem=7
# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def is_prime(n):
    # if n in primes:
    #     return True
    f = 2

    while f < n:
        if n % f == 0 and f != n:
            return False
        f += 1
    # primes.append(n)
    return True

prime_count = 1
stop_number = 10001
val = 3
end_num = 0

while prime_count != stop_number:
    if is_prime(val):
        prime_count += 1
        end_num = val
    val += 2

print(end_num)