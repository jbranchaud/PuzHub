#!/usr/bin/python

# HAMM.py
# http://rosalind.info/problems/hamm/

"""
Given two strings s and t of equal length (which will need to be read from a 
file appearing on subsequent lines), this function will iterate over the
two strings comparing the corresponding symbols in order to compute the
Hamming distance. For each pair of symbols that do not match, the Hamming
distance is increased by 1. The total Hamming distance between the two strings,
s and t, is then returned.
"""

import sys
import itertools

if len(sys.argv) <= 0:
    print "Need to include the input filename."
    sys.exit()

# get the file's name
filename = sys.argv[1]

# open the file as read-only
f = open(filename, 'r')

# read in the first two lines of the given file
dna1 = f.readline()
dna2 = f.readline()

distance = 0

# compute the Hamming distance between the two DNA sequences by comparing
# each corresponding symbol
for s1, s2 in itertools.izip(dna1,dna2):
    if s1 != s2:
        distance += 1

print distance

