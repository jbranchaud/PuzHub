#!/usr/bin/python

# PERM.py
# http://rosalind.info/problems/perm/

"""
Given an int value (which is read in as the first line from the given a file),
this function will first print the number of possible permutations of the
sequence of integers between 1 and the given int and will
then proceed to print on each subsequent line all permutations for that
sequence of integers.
"""

import sys

# Globals
series = []
direction = []

"""
perm_count: integer -> integer
given an integer n that represents the number of characters in a series,
namely 1-n, this function will compute the number of permutations that can be
made with that series and then return the result.
"""
def perm_count(n):
    # there is always at least 1 permutation
    perms = 1
    # compute n! (factorial)
    for i in range(n):
        perms = perms * (i + 1)

    return perms


"""
print_series: none -> void
simply print each value in the series on one line to stdout with single spaces
between each character.
"""
def print_series():
    line = series.__str__()
    line = line.lstrip('[').rstrip(']').replace(',','')
    print line


"""
initialize_lists: integer -> void
given an integer n that represents the number of characters in a series,
namely 1-n, this function will initialize the series and direction global
lists so that they can be used by the Johnson-Trotter algorithm.
"""
def initialize_lists(n):
    for i in range(n):
        series.append(i+1)
        direction.append('<')


"""
john_trot_printer: integer -> void
given an integer n that represents the number of characters in a series,
namely 1-n, this function will use the Johnson-Trotter algorithm to compute
all permutations of that series, printing each to stdout as it goes.
"""
def john_trot_printer(n):
    # initialize the global lists for this algorithm
    initialize_lists(n)

    # print the initial series (before permutations)
    print_series()

    largest_mobile = find_largest_mobile()
    while(largest_mobile != None):
        new_index = swap_item(largest_mobile)
        update_directions(new_index)
        largest_mobile = find_largest_mobile()

        print_series()


"""
find_largest_mobile: none -> integer
this function will go through the current series and direction lists to
determine which in the series is the largest mobile integer. If there exists
such an integer, its current index in series will be returned, otherwise None
will be returned.
"""
def find_largest_mobile():
    largest = 0
    index = None
    for i in range(len(series)):
        if series[i] > largest and is_mobile(i):
            largest = series[i]
            index = i

    return index


"""
update_directions: integer -> void
given an integer that represents the index into the series list, this function
will find all integers larger than the integer at the given index and reverse
their current direction.
"""
def update_directions(index):
    value = series[index]
    for i in range(len(series)):
        if value < series[i]:
            if direction[i] == '<':
                direction[i] = '>'
            else:
                direction[i] = '<'


"""
swap_item: integer -> integer
given an integer that represents the index into the series list, this function
will swap the item at that index with the immediate neighbor in the direction
that it is looking. The new index of the item being swapped will be returned.
This new index is either +1 or -1 of the given integer value.
"""
def swap_item(index):
    index2 = 0
    if direction[index] == '<':
        # swapping to the left
        index2 = index - 1
    else:
        # swapping to the right
        index2 = index + 1

    tmp = series[index2]
    series[index2] = series[index]
    series[index] = tmp

    tmp = direction[index2]
    direction[index2] = direction[index]
    direction[index] = tmp

    return index2


"""
is_mobile: integer -> boolean
given an integer that represents an index into the series list, this function
will determine if it is a mobile integer -- meaning it is larger than its
immediate neighbor in the direction that it is looking -- and then return True
or False accordingly.
"""
def is_mobile(index):
    if direction[index] == '<':
        # looking left
        if index != 0 and series[index] > series[index-1]:
            return True
        else:
            return False

    else:
        # looking right
        if index != len(series)-1 and series[index] > series[index+1]:
            return True
        else:
            return False


if len(sys.argv) <= 0:
    print "Need to include the input filename."
    sys.exit()

# get the file's name
filename = sys.argv[1]

# open the file as read-only
f = open(filename, 'r')

# read in the first line of the file
n = int(f.readline())

print perm_count(n)

john_trot_printer(n)

