#!/usr/bin/python

# template.py
# http://rosalind.info/problems/template/

"""
Given a string of length at most 1000 that contains the characters A, C, G,
and T, this script will go through the string replacing all of the Ts
with Us. The resulting transcribed RNA sequence will be returned as a string.

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


