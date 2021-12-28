#!/usr/bin/env python3

f = open('ctf.orig', 'rb')
data = f.read()
f.close()

l = len(data)


for i in range(64):
    for j in range(240):
        f = open('out/{}-{}.gz'.format(i,j), 'wb')
        f.write(data[0:i] + data[l-j:])
        f.close()
