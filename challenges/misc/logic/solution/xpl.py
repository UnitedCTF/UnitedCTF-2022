#!/usr/bin/python3

CIPHERTEXT = open("./dist/flag.enc", "rb").read()


def encrypt_byte(byte: int, key: int) -> int:
    p_0 = (byte >> 0) & 1
    p_1 = (byte >> 1) & 1
    p_2 = (byte >> 2) & 1
    p_3 = (byte >> 3) & 1
    p_4 = (byte >> 4) & 1
    p_5 = (byte >> 5) & 1
    p_6 = (byte >> 6) & 1
    p_7 = byte >> 7

    c_0 = not (p_1 ^ p_6 ^ ((key >> 0) & 1))
    c_1 = not (p_0 ^ p_7 ^ ((key >> 1) & 1))
    c_2 = not (p_3 ^ p_4 ^ ((key >> 2) & 1))
    c_3 = not (p_5 ^ p_2 ^ ((key >> 3) & 1))
    c_4 = not (p_5 ^ ((key >> 4) & 1))
    c_5 = not (p_4 ^ ((key >> 5) & 1))
    c_6 = not (p_7 ^ ((key >> 6) & 1))
    c_7 = not (p_6 ^ ((key >> 7) & 1))

    return (
        c_0
        | (c_1 << 1)
        | (c_2 << 2)
        | (c_3 << 3)
        | (c_4 << 4)
        | (c_5 << 5)
        | (c_6 << 6)
        | (c_7 << 7)
    )


for key in range(256):
    d = {encrypt_byte(i, key): i for i in range(256)}
    maybe_plaintext = bytearray([d[i] for i in CIPHERTEXT])
    try:
        maybe_plaintext = maybe_plaintext.decode()
        if "FLAG-" in maybe_plaintext:
            print(maybe_plaintext)
            exit(0)
    except:
        pass
