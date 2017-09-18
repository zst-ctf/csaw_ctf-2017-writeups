with open("../encrypted", "r") as file:
    input = file.read().strip()[:-64]

enc_ascii = input.decode("hex")

enc_numbers = [ord(ch) for ch in enc_ascii]

key_len = 26
