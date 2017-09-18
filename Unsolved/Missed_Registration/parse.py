#!/usr/bin/env python3

with open('out2.txt', 'r') as f:
    raws = f.readlines()

#output = open('registrations.txt', 'a')
for line in raws:
    hex = line.split('&n=')[1].strip()
    text = bytes.fromhex(hex).decode()
    if 'flag{' in text:
        print(text)
#        print(hex)
#        raise e

print('Done')
'''
items = line.split('&')

items = items[4:] # remove unnecessary data

lname = items[5]
output.write(entry)
output.write('\n')
'''

#output.close()

