# RFC4648

The flag has been Base64 encoded multiple times.
```bash
a=$(cat challenge.txt); while :; do b=$(echo $a | base64 -d 2>/dev/null) || break; a=$b; done; echo $a
```

# Flag

`FLAG-1l0v3b4s364encod1ng_efd3c54`