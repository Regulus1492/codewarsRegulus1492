# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# Other solutions

# Enumerator is an iterator. It turns the string into a list made out of every letter of the string "c"
# and a conter "i" in this case. 


def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))

# My solution
def accum(st):
    list1 = [i for i in st]
    counter = 0
    string = list1[0].upper()
    for i in list1[1:]:
        counter += 1
        string = string + "-{}".format(i.upper()) + "{}".format(i.lower()*counter)
        
    return string
        
