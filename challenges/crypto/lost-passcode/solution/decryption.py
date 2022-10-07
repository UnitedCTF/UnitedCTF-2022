#Made by Ioarana

import random

result = input ( "Enter public key: " )
private_key = input ( "Enter private key: " )

m = 0
used_rand = ""
result_dec =""
for i in result:
	while (private_key[m] != " "):
		used_rand= used_rand + private_key[m]
		m = m+1
	dec = ord(i)	
	dec = ord(i) - int(used_rand)
	dec = chr(dec)
	dec = str(dec)
	
	result_dec = result_dec + dec
	used_rand=""	
	m = m+1

print("resultat dec:",result_dec)