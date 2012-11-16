#!/usr/bin/python

# DNA.py
# http://rosalind.info/problems/dna/

"""
Given a string of length at most 1000 that contains the characters A, C, G,
and T, this script will count the number of each, and print the number of
each respectively on a single line separated by spaces.

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

# create a dictionary for the letters
nucs = {'A':0, 'C':0, 'G':0, 'T':0}

for nuc in dna:
    if nuc == 'A':
        nucs[nuc] = nucs[nuc] + 1
        continue

    if nuc == 'C':
        nucs[nuc] = nucs[nuc] + 1
        continue

    if nuc == 'G':
        nucs[nuc] = nucs[nuc] + 1
        continue

    if nuc == 'T':
        nucs[nuc] = nucs[nuc] + 1
        continue

print str(nucs['A']) + " " + str(nucs['C']) + " " + str(nucs['G']) + " " + str(nucs['T'])

