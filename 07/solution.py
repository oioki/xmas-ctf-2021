#!/usr/bin/env python3

# https://esolangs.org/wiki/Language_list
# https://esolangs.org/wiki/(%3F!)

f = open('input.txt', 'r')
parts = f.read().split('(!)')


for part in parts:
    part = part[:-1]
    if not part:
        break
    aa = part.split('(')
    bb = aa[1].split(')')
    a = len(aa[0])
    b = len(bb[0])
    c = len(bb[1])
    print(chr(a*b+c), end='')
