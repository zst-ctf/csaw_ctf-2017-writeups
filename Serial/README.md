## Serial
Misc - 50 points

### Challenge 
> nc misc.chal.csaw.io 4239

### Solution

Overall, this is a fun challenge, involving the knowledge of some electronics UART serial communication. 

When nc-ing in, we get this

    8-1-1 even parity. Respond with '1' if you got the byte, '0' to retransmit.
    00110011001

From `8-1-1 even parity` we know this is UART serial communication of 8-bits + 1 stop bit + 1 even parity bit. A retransmission is needed if parity is not even.


A UART Frame can be seen in [this website](https://electricimp.com/docs/resources/uart/)
There are 11 bits provided:

- 1 start bit (always 0)
- 8 char bits
- [1 parity bit](https://en.wikipedia.org/wiki/Parity_bit)
- 1 stop bit (always 1)


I created a [python script](solver.py) and after a few minutes, we get the flag!

    Success - flag{@n_int3rface_betw33n_data_term1nal_3quipment_and_d@t@_circuit-term1nating_3quipment}
