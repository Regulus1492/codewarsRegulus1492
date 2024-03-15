# Instruction

# Write a function, persistence, that takes in a positive parameter num and returns its 
# multiplicative persistence, which is 
# the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

# Recursive Solution 
from operator import mul
import functools 
def persistence(n):
    return 0 if n<10 else persistence(functools.reduce(mul,[int(i) for i in str(n)],1))+1

# Another smart solution
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


# My solution

def persistence(n):
    persistance_num = 1
    def digitmult(n):
            # Base case
            if n == 0:
                return 1
            return (n % 10 * digitmult(n // 10))
    
    def countDigit(n):
        if n // 10 == 0:
            return 1
        return 1 + countDigit(n // 10)
     
    digitmul_res = digitmult(n)
    digitcount_res = countDigit(digitmul_res)
    
    # Checks if number is 1 digit number al ready
    if countDigit(n) == 1:
        persistance_num = 0
    else:
        while digitcount_res > 1:
            digitmul_res = digitmult(digitmul_res)
            digitcount_res = countDigit(digitmul_res)
            persistance_num += 1
            print(n,digitmul_res,digitcount_res,persistance_num)

    return persistance_num

print(persistence(292))