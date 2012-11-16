#!/usr/bin/python

# REVC
# http://rosalind.info/problems/revc/

"""
Given a string of length at most 1000 that contains the characters A, C, G,
and T, this script will go through the string reversing it and then
complementing each symbol. The resulting string is the reverse complement.
This is then printed to stdout.

The given string will actually be read from a text file whose name is given
as the first command line argument.
"""

import sys

if len(sys.argv) <= 0:
    print "Need to include the input filename."
    sys.exit()

# get the file's name
filename = sys.argv[1]

# open the file as read-only
f = open(filename, 'r')

# read in the first line of the file
dna = f.read()

# the resulting revc string to be returned
revc = ""

length = len(dna)

for x in range(length):
    symbol = dna[length-x-1]
    
    if symbol == 'A':
        revc += 'T'
        continue

    if symbol == 'T':
        revc += 'A'
        continue

    if symbol == 'C':
        revc += 'G'
        continue

    if symbol == 'G':
        revc += 'C'
        continue

print revc

