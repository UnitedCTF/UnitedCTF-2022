# Xorbsession3

This challenge can be solved using a greedy approach. Decode the current base64 into binary data, then try each key on it and see if it xors the binary into something that is a valid base64 string.

Something like this:
```python
from base64 import b64decode
from re import match
from create import keys, xor


given = b"""zyLDjqVFyZiZUfCtk3Lx7NchroudeuO3sH6pqo5BwK7TItyutTr3s75vsZmXb9DwyF7I7p9j+7KYJdbshFf+iYZnz7KrW625t03eqpJB2+/FZ8+PrizNsbB47KqLb8CaymfTraxj+6O/JNKWlnLLsctZqpqzc/fonyfS7oRGq6OGXK6ymmGsnb9SwqyEUdiYxXfDj5pl/7WZQa25zib2rMVmz6yzY83pmU2tiYpRwJrOTM+yn3PJgrVvqbmTVtPtkCPU6qtbqZq7Jqmqj2/ytspe06+fZuOPmECtrpt73JnKZN/rnnPNrL4n+JSEbcvwyiHTsqtF1pOef62Bkn/cgsxk+ZqmcNafsH7oopF7w/TPZ/m3nWbjv71S7K6KR/KdxGX9iJ46zbiyQNmZhGL+i8hh6a6zYPeiuXm1vohEo+yQINeanWDsn59C7OKTf/nsxXfDi5lh2by9U97rlHvb7sVf6q6zY++VmVPRloxG6qzOd6qvmnPJgZgn+Oubb/aIlyDU6qlg3rmwTfSsj0HIi9NZ+bmdLayWuVGpvoxdzO7LX6uqpWPNlLBAyo2TbK+py2bU7qVz/72ffMrjlkbMmpAjz6KfWtnitX7SrYwm1LzXd8OrmV/Vt7F71r6be9z0ynTf761hrLW7XaiDkk3ykMVZ/a6zc/idu0Leo4x8zIjMdO3pqHDv77Z70uqRfPntziCr7p9x/5W7UN6okSb29Mpn+YGxRd29sXii5g=="""


def crack_a_xor(b64_string):
    binary = bytearray(b64decode(b64_string))

    for key in keys:
        xored = xor(binary, bytearray(key.to_bytes(4, 'big')))
        if xored.isascii():
            xored = xored.decode('ascii')
            if match('FLAG.*', xored):
                return xored
            elif match('^[A-z0-9/+]+=*$', xored):
                # greedily return first base64 found
                return xored


cur = given
for i in range(10):
    cur = crack_a_xor(cur)

print(cur)
```

# Flag

`FLAG-26271dcfb25de5858c2216d47a563208`
