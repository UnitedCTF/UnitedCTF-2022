from base64 import b64encode
from random import choice


def xor(cur, b):
    res = cur.copy()
    for i in range(len(res)):
        res[i] ^= b[i % len(b)]
    return res


flag = bytearray(b'FLAG-REDACTEDHEXREDACTEDHEXREDACTEDHE')
keys = [0xa93f9c6f,
     0x3032fa89,
     0xc56714be,
     0x031734d4,
     0x649bf77a,
     0x86cf8750,
     0xec4b53c9,
     0x3c83c74a,
     0x3020cd88,
     0x6de08505,
     0xc7c63073,
     0x35205397,
     0x74ff5323,
     0x5d0a23b2,
     0xc3120ca7,
     0xe0b4e70f,
     0xec2775ea,
     0x15e6ef25,
     0x93fb8172,
     0xda3d1099,
     0x70ac81e7,
     0x601dda5a,
     0x4ba6152e,
     0x068c4540,
     0xde28762f,
     0x7e712461,
     0x05c8cc1c,
     0xaf5e5f01,
     0xb718c86e,
     0xa44e5688,
     0x1da6ef8e,
     0x16be54b0,
     0xe6fcf0e5,
     0x32509a73,
     0x812d83c2,
     0x333af163,
     0x451db1bd,
     0x118e688a,
     0x08f05a43,
     0x334bc7de,
     0x1f8ca915,
     0x66ec0cba,
     0x00b6b560,
     0x1ac2b636,
     0x11e500de,
     0x7bf6763e,
     0xc0eee9fe,
     0x9076ce5d,
     0x25b256d2,
     0xb3e835c7,
     0xf85b6823,
     0xc610f2c2,
     0x0b9f2e6a,
     0x2d2fa455,
     0xbf324a9f,
     0xb66ec850,
     0x9634e995,
     0xa7514ca8,
     0xced21bf7,
     0x81205993,
     0x15c76d19,
     0xbbe9e129,
     0x7aeb3d49,
     0xe4b58dc2,
     0x1b62d7e0,
     0x1fca5d88,
     0x73c6641f,
     0x75e332d1,
     0x6d262dcf,
     0x39b66f5b,
     0xd275277f,
     0xa45eafb2,
     0x04ef0ad7,
     0x7b41d942,
     0x9449d114,
     0xce45761d,
     0xfc159adb,
     0x202a1b1d,
     0x04d312b5,
     0x610ad175,
     0x5cfcc191,
     0xb8f44108,
     0x96b80b97,
     0x36774bd6,
     0x8f653774,
     0x6ba8ec6e,
     0xddf01b17,
     0x0dc42e2a,
     0x8092ebde,
     0x2029b4a4,
     0x006875fd,
     0xb1f05cbb,
     0x0b05c77f,
     0x586f63bb,
     0x55f038a9,
     0x674fbe15,
     0x4652dc61,
     0x044e6e0d,
     0x2102a284
] 


if __name__ == '__main__':
     for _ in range(10):
         key = choice(keys)
         # print(hex(key)) # print keys
         flag = xor(flag, bytearray(key.to_bytes(4, 'big')))
         flag = bytearray(b64encode(flag))
     
     print(flag.decode('ascii')) # prints the puzzle input
