#!/usr/bin/env python

import sys
import math

def isprime(n):
    for i in range( 2, int( math.ceil( math.sqrt(n) ) ) + 1 ):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    harmonious = False
    rows = 0
    for line in sys.stdin:
        if '0' in line:
            harmonious = harmonious or isprime(rows)
            if harmonious:
                print 'Harmonious'
            else:
                print 'Cacophonous'
            sys.exit(0)
        rows += 1
        if not isprime(len( line ) - 1):
            print 'Cacophonous'
            sys.exit(0)
