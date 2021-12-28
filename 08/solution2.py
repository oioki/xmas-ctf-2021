#!/usr/bin/env python3

import zlib

for v17 in range(128):
    print(v17)
    for v20 in range(128):
        for v23 in range(128):
            for v26 in range(128):
                _ = bytes([v17, v20, v23, v26])
                if _.decode().isalpha():
                    if v20 - v23 == 3:
                        if v17 - v26 == 13:
                            if zlib.crc32(_) == 1545301773:
                                print(chr(v17), chr(v20), chr(v23), chr(v26))
                                exit()
