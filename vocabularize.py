#!/usr/bin/python

import heapq
import sys
import argparse

vocab = {}

def main(argv):
    parser = argparse.ArgumentParser(description='Vocabularize sentence files')
    parser.add_argument('--vocabulary', metavar='<vocabulary file>', required=True,
                        help='Vocabulary file, containing a word on each line, rest of line will be ignored')
    parser.add_argument('--pad', metavar='N', type=int, help='pad sentences to N words')
    parser.add_argument('--outfile', metavar='<output file>', help='output is written to this file')
    parser.add_argument('--inverse', type=bool, default=False)
    parser.add_argument('files', metavar='<sentence file>', nargs='+',
                        help='sentence files, containing a sentence per line. If less than N words, will be padded by 0, if longer: rejected')

    args = parser.parse_args()

    f = open(args.vocabulary, 'r')
    readvocab(f, args.inverse)

    if args.outfile is not None:
        out = open(args.outfile, 'w')
    else:
        out = sys.stdout

    for sf in args.files:
        f = open(sf, 'r')
        process(f, out, args.pad)

def readvocab(f, inverse):
    i = 1
    for line in f:
        if inverse:
            vocab[str(i)] = line.split()[0]
        else:
            vocab[line.split()[0]] = i
        i += 1
    if inverse:
        vocab['0'] = 'PAD'

def process(f, out, pad):
    for sentence in f:
        tokens = sentence.split()
        if len(tokens) > pad:
            continue
        vs = []
        for token in tokens:
            v = vocab.get(token.lower())
            if v is None:
                break
            vs.append(v)
        else:
            for i in range(pad - len(tokens)):
                vs.append(0)
        if len(vs) == pad:
            out.write(" ".join(str(v) for v in vs) + "\n")



if __name__ == "__main__":
    main(sys.argv[1:])
