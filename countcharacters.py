# The main idea is to count all the occurring characters in a string. If you have a 
# string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

# Other solutions

def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r

def count(s):
    return {x:s.count(x) for x in set(s)}


# my solution

def count(s):
    # They key is the filter funtion
    character_counter = {}
    if s:
        list_s = [i for i in s]
        for value in list(set(list_s)):
            character_counter[value] = len(list(filter(lambda x:x == value, list_s)))    
        return character_counter
            
    else:
        return {}



