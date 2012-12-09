#!/usr/bin/python

# GC.py
# http://rosalind.info/problems/grph/

"""
Given the name of a file that contains a series of DNA strings in FASTA format,
this script will need to create an overlap graph for those DNA strings such
that string s will have a directed edge to string t if a suffix of length k in
s matches a prefix of length k in t. For this problem k is equal to 3.
The resulting graph will need to be printed out in adjacency list format in
any order such that each pair of nodes (v,w) has a directed edge from v to w.
"""

import sys

if len(sys.argv) <= 0:
    print "Need to include the input filename."
    sys.exit()

# get the file's name
filename = sys.argv[1]

# open the file as read-only
f = open(filename, 'r')

k = 3

# create the id-sequence dict
dna_dict = {}
curr_id = ""

for line in f:
    if line.strip() == "":
        continue

    if line.startswith('>'):
        curr_id = line.strip().lstrip('>')
        dna_dict[curr_id] = ""
        continue

    dna_dict[curr_id] = dna_dict[curr_id] + line.strip()

adj_list = []

# build the adjacency list for the overlap graph
for id1, dna1 in dna_dict.iteritems():
    for id2, dna2 in dna_dict.iteritems():
        if id1 != id2:
            if dna1[-k:] == dna2[:k]:
                adj_list.append((id1,id2))

# print the adjacency list
for pair in adj_list:
    print pair[0] + ' ' + pair[1]

