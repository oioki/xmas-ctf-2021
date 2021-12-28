#!/usr/bin/env python3

f = open('weird_traffic.pcap', 'rb')
data = f.read()
f.close()

# 1st symbol: 0x3a
# 2nd symbol: 0xcc
step = 0xcc - 0x3a

for i in range(len(data)//step):
    print(chr(data[0x3a + i*step]), end='')
