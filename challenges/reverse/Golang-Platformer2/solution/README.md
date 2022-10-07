# Golang Platformer 2

## Solution

This challenge use the same binary than the first one so you can go back to your decompiler of choice and look in the functions again. There is a function that catches the eye, it is the `printFlag` function. This one is really short but there is 3 `cmp` instructions that seems a bit sus. They compare theses strange values to something : `7473696E696D6441h`, `6F746172h`, `72h`.You have to decode them, convert them to chars and reverse them, all one by one and concatenate them to get the full string `Administrator`. Now that you have a secret string, you need to put it in the `saveFile.txt`. Once you restart the game, the flag will be print to the console. You can also determine that you have to put the flag there by looking at which function is calling `printFlag`(it is the `checkForSaveFile` one).

## Flag

`FLAG-{SaveFileManipulationIsLit}`
