#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data)!=6:
        continue
    category,cost=data[3],data[4]
    print "{0}\t{1}".format(category,cost)
