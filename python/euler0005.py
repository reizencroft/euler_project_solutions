# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?

def is_divisible(n, val):
    z = n
    while z > 0:
        if val % z != 0:
            return False
        z -= 1
    return True


i = 1
x = 20

test = x * i

# print(is_divisible(10, 2520))

while is_divisible(20, test) == False:
    i += 1
    test = x * i

print(test)