# Baby RSA

We can use `sagemath`'s implementation to factor the modulus.

```python
e = 0x10001
n = 0xac586f447e16c51821999902cf993f47
ciphertext = 0x9b7a8eb8ad559e3f52ff3ceeaf0025a4

p, q = factor(n)
p, q = p[0], q[0]
phi = (p - 1)*(q - 1)
d = inverse_mod(e, phi)

flag = pow(ciphertext, d, n)
flag = bytes.fromhex(hex(flag)[2:]).decode()
print(flag)
```

# Flag

`t0o_sm4l1_effdc8`