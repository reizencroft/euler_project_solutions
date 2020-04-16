# Largest palindrome product
# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def get_digits_array(num):
    q1 = num
    digits = []
    digits.append(int(q1 % 10))
    while q1 != 0:
        q1 = int(q1 / 10)
        if (q1 == 0): break
        digits.append(int(q1 % 10))
    return digits

def is_palindrome(num):
    digs = get_digits_array(num)
    i = 0
    j = len(digs) - 1

    while j >= i:
        # print("%d vs %d" % (digs[j], digs[i]))
        if digs[j] != digs[i]:
            return False
        j -= 1
        i += 1
    return True


# digits_array = get_digits_array(1234567)
# for digit in digits_array:
#     print(digit)

# print(is_palindrome(9019))
# print(is_palindrome(9009))
# print(is_palindrome(90009))

num1 = 999
num2 = 999
biggest = 0
while num1 > 99:
    while num2 > 99:
        test = num1 * num2
        # print(test)
        if is_palindrome(test) and test > biggest:
            biggest = test
        num2 -= 1
    num1 -= 1
    num2 = num1

print("Biggest %d" % biggest)