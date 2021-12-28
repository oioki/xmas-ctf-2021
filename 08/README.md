# Day 8. PYO

> Last year, an elf made a perfect program for Santa. Now he has to change it but he lost the source code. Please help him to reverse this compiled program.

IMPORTANT: The flag for this challenge is not in the standard competition format.

[1.pyo.7z](./1.pyo.7z)

## Solution

Not sure if it was a part of challenge, but the actual PYO file was archived with `7z` compressor. Again, we have a compiled Python code:

```
$ file 1.pyo 
1.pyo: python 3.6 byte-compiled
```

However, unlike [Day 5](../05/README.md), we cannot use `decompyle3` because it only supports Python 3.7+, so I had to use a different Python decompiler:

```
$ sudo apt install python3.6
$ python3.6 -m pip install uncompyle6
$ uncompyle6 1.pyo > 1.py
```

See [decompiled code](./1.py).

So, the flag consists of characters that are encoded either with Base64, hexlify, or CRC. With the first two it is more or less obvious what to do. See [first part of the solution](./solution1.py):

```
$ ./solution1.py
bytearray(b'flag{h3x_b4se64_cRc_?he?3w?r}?')
```

As of CRC, it is a relatively fast algorithm, so we can try to bruteforce the required condition. With something like [this](./solution2.py):

```
$ ./solution2.py
0
1
2
...
82
R w t E
```

Putting the pieces together, we get the flag:

```
flag{h3x_b4se64_cRc_whet3wEr}
```
