#!/usr/bin/env python3

from binascii import unhexlify
from base64 import b64decode

v = bytearray(b'?'*30)

a = unhexlify(b'66673362655f6368337261685f')

b = b64decode(b'bHt4NDZjX2V3fXM0Ug==')

v[0] = a[0]
v[3] = a[1]
v[6] = a[2]
v[9] = a[3]
v[12] = a[4]
v[15] = a[5]
v[18] = a[6]
v[21] = a[7]
v[24] = a[8]
v[27] = a[9]
v[2] = a[10]
v[5] = a[11]
v[8] = a[12]

v[1] = b[0]
v[4] = b[1]
v[7] = b[2]
v[10] = b[3]
v[13] = b[4]
v[16] = b[5]
v[19] = b[6]
v[22] = b[7]
v[25] = b[8]
v[28] = b[9]
v[11] = b[10]
v[14] = b[11]
v[17] = b[12]

print(v)
