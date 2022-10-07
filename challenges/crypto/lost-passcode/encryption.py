#Made by https://www.codegrepper.com/code-examples/python/encryption+algorithms+in+python

import random

text = input ( "Enter text: " )

result = ""
private_key = ""

for i in text:

    rand = random.randint ( 1, 125 )
    en = rand + ord ( i )
    en = chr ( en )
    en = str ( en )

    private_key = private_key + str ( rand ) + " "

    result = result + en

print ( "\nPublic key:", result )
print ( "Private key:", private_key )