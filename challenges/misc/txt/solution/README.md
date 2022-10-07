# TXT

```bash
dig -t txt +short ctf.unitedctf.ca | tr -d '"' | awk -F= '{print $2}' | base64 -d
```

# Flag

`FLAG-4eef1b53ba09dfd7fdb7037b488839770`