#!/usr/bin/python

# RNA.py
# http://rosalind.info/problems/subs/

"""
Given two strings s and t of length at most 1000 that represent DNA sequences,
this script will go through s and find all occurrences of substring t. The
substrings will be recorded by the base 1 index of the first character of the
substring. The resulting list of substring positions will be printed with a
space between each.

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
s = f.readline().strip()
t = f.readline().strip()

positions = []

substart = 0

while True:
    substart = s.find(t,substart)
    if substart == -1:
        break
    substart += 1
    positions.append(str(substart))

if positions:
    print " ".join(positions)

