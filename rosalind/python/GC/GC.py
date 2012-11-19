#!/usr/bin/python

# GC.py
# http://rosalind.info/problems/gc/

"""
Given the name of a file that contains a series of DNA strings in FASTA format,
this script will need to determine which of the DNA strings has the highest
GC content. The output should then be the ID of the DNA sequence followed on
the next line by the percentage of the GC content. The percentage must be
accurate to 4 decimal places to the actual answer.
"""

import sys
import decimal


"""
get_gc_content: string -> Decimal
given a string that represents a DNA sequence, this function will determine
the GC content of that sequence and return it in the form of a Decimal
percentage.
"""
def get_gc_content(dna):
    gc_count = 0
    count = 0

    for symbol in dna:
        count += 1
        if symbol == 'C' or symbol == 'G':
            gc_count += 1

    return decimal.Decimal(gc_count) / decimal.Decimal(count)


# set the precision at 6, we don't need more than that
decimal.getcontext().prec = 8

if len(sys.argv) <= 0:
    print "Need to include the input filename."
    sys.exit()

# get the file's name
filename = sys.argv[1]

# open the file as read-only
f = open(filename, 'r')

# create the id-sequence and id-decimal dicts
dna_dict = {}
decimal_dict = {}
curr_id = ""

for line in f:
    if line.strip() == "":
        continue

    if line.startswith('>'):
        curr_id = line.strip().lstrip('>')
        dna_dict[curr_id] = ""
        continue

    dna_dict[curr_id] = dna_dict[curr_id] + line.strip()

max_id = ""
max_value = decimal.Decimal(0)

# calculate the percentages for each dna sequence
for key, value in dna_dict.iteritems():
    #decimal_dict[key] = get_gc_content(value)
    tmp_value = get_gc_content(value)
    #print key + " - " + tmp_value.__str__()
    if tmp_value > max_value:
        max_value = tmp_value
        max_id = key

max_pert = decimal.Decimal(100) * max_value

print max_id
print max_pert.__str__() + "%"

