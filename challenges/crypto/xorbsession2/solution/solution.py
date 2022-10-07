from base64 import b64decode
from requests import get


def xor(cur, b):
    for i in range(len(cur)):
        cur[i] ^= ord(b[i % len(b)])
    return cur


cipher = b64decode('XWxPUD5HSBhAR1gHVnh9b31mNUg=')
url = 'https://raw.githubusercontent.com/ntnco/dictionnaire/main/dictionary.csv'
text = get(url).text.splitlines()

cur = [ord(c) for c in cipher.decode('ascii')]

for line in text:
    cur = xor(cur, line)

res = b''.join([n.to_bytes(1, 'big') for n in cur])
print(res.decode('ascii'))
