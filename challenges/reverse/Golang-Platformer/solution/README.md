# Golang Platformer 1

## Solution
The description challenge you to go West in the game, but you see that the player is always going right and you there is no button to change direction. So use a disassembler like IDA Freeware or Ghidra to try and understand what it does. In the functions, theres a function called `main_run` that is the heart of the program and in the beginning of that function, you can see a variable `cs:flag_CommandLine` followed by a string `runSpeedMulitplier`. So you can deduct there is a command line argument name runSpeedMultiplier that if you provide a negative number to it you are able to change the direction of you caracter. Then you start the game again with -runSpeedMultiplier=-1 and you see the flag in the background in the game.

## Flag

`FLAG-PlatformerGoesrrrB`