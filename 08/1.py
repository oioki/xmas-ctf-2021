# uncompyle6 version 3.8.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.15 (default, Sep 10 2021, 00:26:58) 
# [GCC 9.3.0]
# Embedded file name: 1.py
# Compiled at: 2021-12-01 20:49:55
# Size of source mod 2**32: 594 bytes
import base64, binascii, zlib
v = input('> ').strip().encode()
if len(v) == 29:
    if binascii.hexlify(bytes([v[0], v[3], v[6], v[9], v[12], v[15], v[18], v[21], v[24], v[27], v[2], v[5], v[8]])) == b'66673362655f6368337261685f':
        if base64.b64encode(bytes([v[1], v[4], v[7], v[10], v[13], v[16], v[19], v[22], v[25], v[28], v[11], v[14], v[17]])) == b'bHt4NDZjX2V3fXM0Ug==':
            _ = bytes([v[17], v[20], v[23], v[26]])
            if _.decode().isalpha():
                if v[20] - v[23] == 3:
                    if v[17] - v[26] == 13:
                        if zlib.crc32(_) == 1545301773:
                            print('OK')
# okay decompiling 1.pyo
