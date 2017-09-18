#!/usr/bin/env python
from almostxor_mod import *

c = '809fdd88dafa96e3ee60c8f179f2d88990ef4fe3e252ccf462deae51872673dcd34cc9f55380cb86951b8be3d8429839'.decode('hex')


def solve():
    k = '62deae51872673dcd34cc9f55380cb86951b8be3d8429839'.decode('hex')
    # try n from 1 to 7 inclusive
    for n in xrange(1, 8): 
        m = decrypt(k, c, n)
        print m
        #quit()


def try_progressive(possibilities, trim=1):
    new_possibilities = {}
    for ascii in xrange(256):
        k = chr(ascii)
        for n in possibilities.keys(): 
            m = decrypt(possibilities[n] + k, c, n)
            if m.startswith('flag{'[:trim]):
                new_possibilities[n] = possibilities[n] + k
                print m, "| n =", n, "| *k =", new_possibilities[n]

    print '--------------------------------------'
    if trim >= len('flag{'): quit()
    try_progressive(new_possibilities, trim + 1)

'''
    for k0 in xrange(256):
        for k1 in xrange(256):
            k = chr(k0) + chr(k1)
            for n in xrange(1, 8): 
                m = decrypt(k, c, n)
                if m.startswith('fl'):
                    print m, "| n =", n, "| k =", k0, k1
'''
possibilities = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: '',
    7: ''
}
try_progressive(possibilities)
    

