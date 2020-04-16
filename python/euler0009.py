# https://projecteuler.net/problem=9
# Special Pythagorean triplet

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def is_pytha(a, b):
    c2 = a*a + b*b
    c = int(math.sqrt(c2))
    if (c*c) < c2:
        return (False, 0)

    return (True, c)

res = is_pytha(1, 1000)

print(res[0])
print(res[1])

xa = 1
xb = 2
xc = 0

while xa < 400:
    while xb < 500:
        res = is_pytha(xa, xb)
        if res[0] == True and (xa + xb + res[1]) == 1000:
            xc = res[1]
            break
        xb += 1
    if xc != 0:
        break
    xa += 1
    xb = xa + 1


print("a=%d, b=%d, c=%d" % (xa, xb, xc))
print(xa*xb*xc)
