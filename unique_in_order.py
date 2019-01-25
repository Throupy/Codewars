from itertools import groupby

#Implement the function unique_in_order which takes as argument a sequence and returns a list of
#items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

print(unique_in_order('AAAABBBCCDAABBB'))
