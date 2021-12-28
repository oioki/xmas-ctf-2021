#!/usr/bin/env python3

import binascii
import base64

f = open('dump.0.eq', 'rb')
lines = f.readlines()
f.close()


for line in lines:
    try:
        payload = base64.b64decode(line)
        print(binascii.hexlify(payload))
    except:
        pass
