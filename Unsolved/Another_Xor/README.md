## Another Xor
Crypto - 100 points

### Challenge 
> Hey, hey can you find my secret.
> UPDATE 10:13 Eastern: the flag is whatever is in sys.argv[2]

[cipher.py](cipher.py)
[encrypted](encrypted)

### No solution :(

I tried kasiski analysis with no luck and also tried bruteforcing but it will take too long.

Here's what I know:

- text in the [encrypted](encrypted) file has 274 hex-encoded chars (137 hex-pairs).
- XOR key is applied to the `text + key + md5(text + key)`
- md5 is 128-bits or 32 chars, `text + key` is 137 - 32 = 105 chars long
- all hex-pairs in encrypted are below 0x80 (ie. they are 7 bit ascii text XOR with 7 bit ascii key)
