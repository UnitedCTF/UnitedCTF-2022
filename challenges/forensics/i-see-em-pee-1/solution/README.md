# I See 'em Pee 1

The flag was encoded in the TTL (Time to Live).
```bash
tshark -r dist/i-see-em-pee-1.pcapng -Y "ip.src == 13.37.13.37" -T fields -e ip.ttl | while read char; do
    printf \\$(printf "%o" $char)
done
```

# Flag
`FLAG-1_th0ugh7_1cmp_w4s_us3l3ss`
