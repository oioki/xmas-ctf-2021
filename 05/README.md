# Day 5. Super Easy Keygen

> Santa used this keygen, so his password would be more secure. Did he succeed?

[SuperEasy.pyc](./SuperEasy.pyc)

## Solution

Quick reconnaissance, what is this file:

```
$ file SuperEasy.pyc 
SuperEasy.pyc: python 3.7 byte-compiled
```

Decompyle3 is a good enough tool to decompile this:

```
$ pip3 install decompyle3
$ python3.7 ~/.local/bin/decompyle3 SuperEasy.pyc > SuperEasy.py
```

See [decompiled source](./SuperEasy.py).

Seems like the correct password (which is also a flag) should pass all boolean checks like `passwd[N] == 'c'`. Let's approach this directly, filter out the needed lines and sort them by the password character index:

```
$ grep 'if passwd' SuperEasy.py | sed 's/.*if passwd\[//' | sort -n
:4] == 'ctf{':
4] == 'S':
5] == 'u':
6] == 'p':
7] == '3':
8] == 'r':
9] == sep:
10] == 'e':
11] == '4':
12] == 's':
13] == passwd[22]:
13] == 'Y':
14] == sep:
14] == sep:
15] == 'k':
15] == 'K':
16] == passwd[19]:
17] == 'y':
18] == 'G':
19] == '3':
19] == passwd[7]:
20] == 'n':
21] == sep:
22] == 'Y':
23] == 'u':
23] == 'u':
24] == '5':
24] == '5':
25] == '}':
```

After collecting all characters and substituting `sep` with `_`, we get the flag:

```
ctf{Sup3r_e4sY_K3yG3n_Yu5}
```
