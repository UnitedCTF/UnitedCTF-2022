from base64 import b64decode
from requests import get


def xor(cur, b):
    for i in range(len(cur)):
        cur[i] ^= b[i % len(b)]
    return cur


cipher = b64decode('XWxPUD5HSBhAR1gHVnh9b31mNUg=')
url = 'https://raw.githubusercontent.com/ntnco/dictionnaire/main/dictionary.csv'
text = get(url).text.splitlines()
cur = bytearray(cipher)

for line in text:
    cur = xor(cur, bytearray(line, encoding='UTF-8'))

print(cur.decode('ascii'))
