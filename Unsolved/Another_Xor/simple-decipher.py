
def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]

def xor_repeated(plaintext, key):
    return xor(plaintext, repeat(key, len(plaintext)))


def decode(key_hex, text_hex):
    key = key_hex.decode('hex')
    text = text_hex.decode('hex')
    cipher = xor_repeated(text, key)
    return cipher
    # .encode('hex')


with open('encrypted', 'r') as f:
    encrypted = f.read().strip()

text_hex = encrypted[:-64]
assert len(text_hex) == 105*2

key_hex = '4120717561'#'4120717561'
orig_key = key_hex.decode('hex')

for i in xrange(1000):
    key_len = len(key_hex) / 2
    result = decode(key_hex, text_hex)

    #if (result[:-key_len].endswith('}')):
    #if ('}' in result[:-key_len]):
    if (orig_key in result):
        print '--------------------'
        print 'i:', i
        print 'Fuzz Key:', key_hex
        print 'Text Hex:', result.encode('hex')
        print 'Text Raw:', result
        #quit()
    key_hex += "aa"

print "No luck!"