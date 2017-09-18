## Almost Xor
Crypto - 200 points

### Challenge 
> Can you decode this ciphertext?
>`809fdd88dafa96e3ee60c8f179f2d88990ef4fe3e252ccf462deae51872673dcd34cc9f55380cb86951b8be3d8429839`
> [almostxor.py](almostxor.py)

### Unsolved

Inside [almostxor_mod.py](almostxor_mod.py) I added comments of what I understand of the function. I also created my own decrypt function which works perfectly (Well, almost... There's some garbage characters due to padding)

	>>> from almostxor_mod import *
	>>> x = encrypt("key", "Hi, I'm zst123", 4)
	>>> decrypt("key", x, 4)
	"Hi, I'm zst123\x97\xa5"

Now, I'm just stuck with finding out the key `k` and the length `n`

This is technically not a XOR cipher since it is just adding up the bits and discarding carry-over bits. So I can't use pre-made tools for frequency analysis.