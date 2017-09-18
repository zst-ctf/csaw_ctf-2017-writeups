#!/usr/bin/env python
import hashlib
import sys
import itertools
import string
import threading

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]

def xor_repeated(plaintext, key):
    return xor(plaintext, repeat(key, len(plaintext)))

def rotate_text(text):
    return text[1:] + text[0]

with open('encrypted', 'r') as f:
    input_hex = f.read().strip()

text = input_hex.decode('hex')
iter = 0
while True:
    print 'Iter:', iter
    iter += 1

    prev = text
    text = xor_repeated(text, rotate_text(text))
    if '\x00\x00' in text:
        print 'Stopping'
        print 'Previous:', prev.encode('hex')
        print 'Current:', text.encode('hex')
        quit()

'''
key = sys.argv[1]
text = input_hex.decode('hex')
cipher = xor_repeated(text, key)
print cipher.encode('hex')
'''