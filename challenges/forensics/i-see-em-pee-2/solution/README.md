# I See 'em Pee 2

An ELF binary was sent through the ICMP payload chunk by chunk.
```bash
tshark -r dist/i-see-em-pee-2.pcapng -Y "ip.src == 13.37.13.37" -T fields -e data | cut -c17-48 | tr -d "\n" | xxd -p -r > out && chmod +x out && ./out && rm -f out
```

# Flag
`FLAG-th1s_c0uld'v3_b33n_s0m3th1ng_m4l1ci0us`
