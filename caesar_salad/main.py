#!/usr/bin/env python

import sys

if __name__ == '__main__':
    begin = True
    counter = 0
    numLines = 0
    for line in sys.stdin:
        if begin:
            # skip first line
            begin = False
            numLines = int(line[:-1])
            continue
        counter = counter + 1
        if counter > numLines:
            sys.exit(0)
        for c in line:
            if c == ' ':
                sys.stdout.write(' ')
            elif c == '\n':
                sys.stdout.write('\n')
            else:
                d = ord(c) + 13
                if d > ord('Z'):
                    d = d - ord('Z') + ord('A') - 1
                sys.stdout.write(chr(d))

