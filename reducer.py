#!/usr/bin/python

import sys

total=0
oldcategory=None

for line in sys.stdin:
    data=line.strip().split("\t")

    if len(data)!=2:
    continue

    category,cost =data

    if oldcategory and category!=oldcategory:
        print "{0}\t{1}".format(oldcategory,total)
        total=0
        oldcategory=category

    total+=float(cost)
    oldcategory=category

if oldcategory!=None:
    print category, "\t", total
