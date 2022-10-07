# XD

```bash
xxd -p -c4 XD.xd | sed 's/[ac]/ /g'

# or

xxd -c4 XD.xd | awk '{print $2,$3}' | tr -c '8\n' ' '
```

# Flag
`FLAG-H3X3DITORS4THEWIN`
