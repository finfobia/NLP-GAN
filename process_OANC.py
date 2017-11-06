#!/usr/bin/python

import sys, getopt, re

ngramfiles = {}

MAXN = 15

def main(argv):
    for arg in argv:
        print "Processing file %s" % arg
        f = open(arg, 'r')
        process(f)

    for n,f in ngramfiles.iteritems():
        f.close()



KOMMA = ' KOMMA '
def process(f):
    cursentence = ''
    for line in f:
        print 'Processing line [%s]' % line
        line = line.replace(',', KOMMA)
        line = line.replace(';', '.')
        line = line.replace('"', '.')
        line = line.replace('\n', ' ')

        subs = line.split('.', 1)
        while len(subs) > 1:
            cursentence += ' ' + subs[0]

            process_sentence(cursentence)
            cursentence = ''
            subs = subs[1].split('.', 1)
        cursentence += subs[0]


VALID_CHARS_RE = re.compile("^[\sa-zA-Z'-]+$")
def process_sentence(s):
    print "Processing [%s]" % s
    if not VALID_CHARS_RE.match(s):
        print "Invalid chars."
        return

    tokens = s.split()
    n = len(tokens)
    if n < 3:
        return

    if n > MAXN:
        print "Too many chars (%d > %d)." % (n, MAXN)
        return


    if ngramfiles.get(n) is None:
        filename = "ngram-%0d.txt" % n
        print "Opening file %s" % filename
        f = open(filename, 'w')
        ngramfiles[n] = f

    f = ngramfiles[n]

    line = " ".join(tokens) + "\n"
    print "%d-gram: %s" % (n, line)
    f.write(line)


if __name__ == "__main__":
    main(sys.argv[1:])