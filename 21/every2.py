#!/usr/bin/env python3

import sys

filename = sys.argv[1]

f = open(filename, 'rb')
data = f.read()
f.close()


data2 = data[0::2]
f = open(filename + '.0', 'wb')
f.write(data2)
f.close()

data2 = data[1::2]
f = open(filename + '.1', 'wb')
f.write(data2)
f.close()
