#!/usr/bin/env python

import sys


if __name__ == '__main__':
    numLines = 0
    begin = True
    lineCounter = 0
    for line in sys.stdin:
        if begin:
            numLines = int(line[:-1])
            begin = False
        elif lineCounter >= numLines:
            sys.exit(0)
        else:
            entry = line[:-1].split(' ')
            s = 0
            for n in entry[2]:
                s += int(n)
            if s == 25:
                print 'ENTRY DENIED'
            elif entry[3] in ('BYTELANDIA', 'LEROY', 'JENKINS', 'FLATLAND'):
                print 'ENTRY DENIED'
            else:
                print 'CAUSE NO TROUBLE', entry[1], entry[0]
            lineCounter += 1


