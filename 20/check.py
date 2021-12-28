#!/usr/bin/env python3

import binascii

p = 87255058923913
q = 88888888888889
r = 3059220303001

c1 = 34352437591853
c2 = 81397125806846
c3 = 2725390340272

m = 74307973

assert c1 == (m**3) % p
assert c2 == (m**3) % q
assert c3 == (m**3) % r

print(binascii.unhexlify(str(m)))
