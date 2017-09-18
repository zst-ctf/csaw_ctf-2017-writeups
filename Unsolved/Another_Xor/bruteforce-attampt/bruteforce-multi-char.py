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


with open('encrypted', 'r') as f:
    cipher_hex = f.read().strip()

cipher = cipher_hex.decode('hex')
cipher_no_md5 = cipher[:-32] # remove 32 chars of MD5
cipher_only_md5 = cipher[-32:]

len_cipher_no_md5 = len(cipher_no_md5)
assert len(cipher_no_md5) == (137 - 32)

# ASCII 0x00 to 0xFF inclusive
chars = string.printable#[chr(i) for i in xrange(0xFF + 1)]

def bruteforce_key(len):
    for guess in itertools.product(chars, repeat=len):
        yield ''.join(guess)

def checkValid(cipher, key, cipher_len, semaphore):
    if semaphore is not None: semaphore.acquire()
    decipher = xor(cipher, repeat(key, cipher_len))
    if all(c in string.hexdigits for c in decipher):
        print key
        print decipher
        quit()
    if semaphore is not None: semaphore.release()


semaphore = threading.Semaphore(value=1000)

for length in xrange(3, 10):
    print "Doing length", length
    for key in bruteforce_key(len=length):
        semaphore.acquire()
        threading.Thread(name='Worker'+str(key), target=checkValid,
            args=(cipher_only_md5, key, len_cipher_no_md5, semaphore)).start()
        semaphore.release()
        '''
        decipher = xor(cipher_only_md5, repeat(key, len_cipher_no_md5))
        if all(c in string.hexdigits for c in decipher):
            print key
            print decipher
            quit()
        '''

'''
for length in xrange(2, 10):
    print "Doing length", length
    for key in bruteforce_key(len=length):
        decipher = xor(cipher_no_md5, repeat(key, len(cipher_no_md5)))
        if ('\n' not in decipher) and key in decipher:
            print key
            print decipher
            quit()
'''