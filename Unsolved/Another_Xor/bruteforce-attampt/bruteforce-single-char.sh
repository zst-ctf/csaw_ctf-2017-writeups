#!/bin/bash
CIPHER_TEXT=$(cat encrypted | xxd -r -p)

for i in {0..255}; do
	echo "Doing key $i"
	# https://unix.stackexchange.com/a/44749
	key=$(printf "\x$(printf "%x" $i)")
	result=$(python cipher.py $key $CIPHER_TEXT)
	result_decoded=$(echo $result | xxd -r -p)
	echo $result_decoded

	# https://stackoverflow.com/questions/2172352/in-bash-how-can-i-check-if-a-string-begins-with-some-value
	if [[ $result_decoded == flag{* ]]; then
		echo $key
		echo $result_decoded
		exit 0
	fi
done

