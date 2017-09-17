#!/usr/bin/env python3
import socket
import string
import re
from multiprocessing.pool import ThreadPool


def attempt(tag, payload, block_number=0):
    s = socket.socket()
    s.connect(('crypto.chal.csaw.io', 1578))

    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            continue
        #print("Received >>", data)

        if 'Enter your username' in data:
            s.send(payload.encode())
            s.send(b'\n')
        if 'Your Cookie is: ' in data:
            cookie = re.search(r'Your Cookie is: (.+)', data).group(1)
            return (tag, cookie[block_number * 32 : block_number * 32 + 32])


def main(progress='', block_number=0):
    block = 'A' * 16

    for skip in range(16):
        prefix = block[skip+1:]

        # Enter 15 characters and retrieve the first 16 encoded
        _, aim = attempt('', prefix, block_number)

        pool = ThreadPool(processes=25)
        async_results = []

        # Then enter 16 characters changing the last one until you get the
        # same result as with 15 characters for the first 16 encoded bytes
        for ch in string.printable:
            payload = prefix + progress + ch

            async_result = pool.apply_async(attempt, (ch, payload, block_number))
            async_results.append(async_result)
            
        # That 16th character is the first character of your secret. 
        # You can then repeat the process by putting 14 characters and then
        # finding the second secret characters with the same thechnique.
        for async_result in async_results:
            ch, result = async_result.get()
            print(f"Result: {ch}, {result} == {aim}")

            if result == aim:
                progress += ch
                if ch == '}':
                    # end of flag! if we continue we
                    # merely get '0's added forever
                    print(f"Success! {progress}")
                    quit()
                break

        print(f"Progress (Block {block_number} of index {skip}): {progress}")

    # continue to next block
    main(progress, block_number + 1)

main()