# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single 
# N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

# Other solutions

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]


def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


# My solution

def find_outlier(integers):
    if not integers:
        return None
    else:
        even_counter = 0
        for value in integers:
            if value % 2 == 0:
                even_counter += 1
        if even_counter == 1:
            return list(filter(lambda x: x % 2 == 0, integers))[0]
        else: 
            return list(filter(lambda x: x % 2 != 0, integers))[0]