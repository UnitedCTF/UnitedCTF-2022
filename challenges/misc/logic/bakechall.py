#!/usr/bin/python3

PLAINTEXT = """\
So, did you brute force this, or you used a pen and a paper?
FLAG-ASIC_R0CK$_2fda8b6cdef1
"""


def encrypt_byte(byte: int, key: int = 42) -> int:
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


ciphertext = bytearray([encrypt_byte(ord(char)) for char in PLAINTEXT])
open("./dist/flag.enc", "wb").write(ciphertext)
