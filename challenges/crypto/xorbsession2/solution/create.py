from base64 import b64encode
from requests import get


def xor(cur, b):
    for i in range(len(cur)):
        cur[i] ^= ord(b[i % len(b)])
    return cur


url = 'https://raw.githubusercontent.com/ntnco/dictionnaire/main/dictionary.csv'
text = get(url).text.splitlines()

flag = 'FLAG-Pr0g_I5_Ur_Fr3n'

cur = [ord(c) for c in flag]
for line in text:
    cur = xor(cur, line)

res = b''.join([n.to_bytes(1, 'big') for n in cur])

cipher = b64encode(res).decode('ascii')

print(cipher)
