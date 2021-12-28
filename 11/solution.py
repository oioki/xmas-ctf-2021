#!/usr/bin/env python3

nums = [-49, -4, 7, -10, -16, -8, -4, 3, -41, -14, -7, -14, -5, -16, -14, -8, -49, -7, -10, 1, 7, -14, -5]

#randkey = 170

for randkey in range(23,2300):
    try:
        #print(randkey, end='')
        for n in nums:
            print(chr(n+randkey-55), end='')
        print()
    except:
        print()
        pass
