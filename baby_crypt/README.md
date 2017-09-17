## baby_crypt
Crypto - 350 point

### Challenge 
> The cookie is `input + flag` AES ECB encrypted with the sha256 of the flag as the key.

`nc crypto.chal.csaw.io 1578`

### Solution
It is given that the key is always static (sha256 of the flag). We have control over the plaintext input.

Hence, this leads me to the [AES/ECB chosen-plaintext attack](https://crypto.stackexchange.com/questions/42891/chosen-plaintext-attack-on-aes-in-ecb-mode). This abuses the fact that AES has a block size of 16 bytes.

With this, we can bruteforce with a [changing 16th byte](https://security.stackexchange.com/questions/62078/how-are-chosen-plaintext-attacks-against-ecb-implemented-in-the-real-world) to see if the results match.

With my initial code, I could only get the first block (ie. only 16 bytes): `flag{Crypt0_is_s`
To find the next block, I modified my code according to [this stackoverflow answer which I find pretty comprehensive](https://security.stackexchange.com/questions/102104/aes-ecb-chosen-plaintext-attack-with-long-secret).

	1. Get the first secret block
	Enter 15 characters and retrieve the first 16 encoded bytes Then enter 16 characters changing the last one until you get the same result as with 15 characters for the first 16 encoded bytes. That 16th character is the first character of your secret. You can then repeat the process by putting 14 characters and then finding the second secret characters with the same thechnique.

	2. Get the second secret block
	You already found the first 16 secret bytes. Now enter 15 characters and find the result for the second block of encoded bytes; bytes 17 to 32. Then enter 32 characters, only changing the last one until you find the 17th secret characters in the secret string. Then repeat to find the 18th and so on byte.


Note: This is my first time trying out `ThreadPool`s in Python so pardon my messy code.

Run [aes-bruteforce.py](aes-bruteforce.py)
`time python3 ./aes-bruteforce.py`

Here's the final snippet after running the script.

	Result: }, e3725519adb9e6f10d658d87c80825ed == e3725519adb9e6f10d658d87c80825ed
	Success! flag{Crypt0_is_s0_h@rd_t0_d0...}

	real	1m59.534s
	user	0m6.434s
	sys	0m4.137s

***Flag: `flag{Crypt0_is_s0_h@rd_t0_d0...}`***