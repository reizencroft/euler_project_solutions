# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 1 
# and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the sum of the even-valued terms.
import sys

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n-1) + fib(n-2)

def fib2(arr, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in arr:
        return arr[n]
    val = fib2(arr, n-1) + fib2(arr, n-2)
    arr[n] = val
    return val
    

fib_arr = {}

max_value = 4000000
term = 1
fib_value = 0
sum_term = 0
i = 1

while term < max_value:
    try:
        term = fib2(fib_arr,i)
        if (term % 2 == 0):
            sum_term += term
        i += 1
    except:
        print(i)
        sys.exit

print("Sum %d (max terms %d)" % (sum_term, i))

