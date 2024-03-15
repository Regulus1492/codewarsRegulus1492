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