#!/usr/bin/python3
from random import randint
import signal
import os

FLAG = os.getenv("FLAG")
ROUNDS = 100
TIMEOUT = 10


def alarm_handler(signum, frame):
    print("Too slow!")
    exit(0)


print(f"Can you solve {ROUNDS} simple equations in less than {TIMEOUT} seconds?")
signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(TIMEOUT)

for i in range(1, ROUNDS + 1):
    a, x, b, = (
        randint(-1337, 1337),
        randint(-1337, 1337),
        randint(-1337, 1337),
    )
    c = a * x + b
    print(f"Round {i:>3}: {a}*x {'+-'[b < 0]} {abs(b)} = {c}")
    answer = input("Answer: ")
    try:
        if int(answer) != x:
            print("Wrong!")
            break
    except:
        print("Invalid input, good bye!")
        break
else:
    print(FLAG)
