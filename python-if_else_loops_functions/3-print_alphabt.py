#!/usr/bin/python3
for alphab in range(97, 123):
    if chr(alphab) not in ['q', 'e']:
        print("{}".format(chr(alphab)), end="")
