## CVV
Misc - 100 points

### Challenge 
> Hey fam, you got CVV? I need some CVV!
`nc misc.chal.csaw.io 8308`

### Solution
When nc-ing into it, the program asks for credit card numbers

It also checks for the length to be 16 digits
	
	I need a new Discover!
	1
	That's not even the right amount of numbers... 

	I need a new Visa!
	1111222233334444
	Hmmmmm that doesn't seem correct...

16-digits tells us we need to give it a unique credit card number for each iteration.
We can use [this website to generate valid but fake credit card numbers](http://www.getcreditcardnumbers.com/credit-card-generator) for Discover, Visa, MasterCard and American Express.

After a few iterations, it starts asking for card starting / ending with a certain number and validity

	I need a new card that starts with 1698!
	I need a new card which ends with 7!
	I need to know if 9132577709294382 is valid! (0 = No, 1 = Yes)

I used [this wonderful Python3 library by @joshleeb](https://github.com/joshleeb/creditcard) to generate the credit card numbers and check validity.

Run [solver.py](solver.py)

***Flag: `flag{ch3ck-exp3rian-dat3-b3for3-us3}`***