#!/usr/bin/python

import heapq
import sys

wordcount = {}

N = 5000

def main(argv):
    for arg in argv:
        print "Processing file %s" % arg
        f = open(arg, 'r')
        process(f)
        f.close()

#    print wordcount
    tops = heapq.nlargest(N, wordcount.items(), lambda x: x[1])
#    print tops

    f = open('vocab', 'w')
    for s in tops:
        f.write("%s %d\n" % (s[0],s[1]))
    f.close()

def process(f):
    for line in f:
        for t in line.split():
            t = t.lower()
            if wordcount.get(t) is None:
                wordcount[t] = 1
            else:
                wordcount[t] = wordcount[t] + 1


if __name__ == "__main__":
    main(sys.argv[1:])
