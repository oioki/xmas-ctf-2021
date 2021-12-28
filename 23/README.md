# Day 23. Nik's message

> Santa is trying to read a wish from one of his top 10 on his nice list. Can you help him read his wish.

[ctf.gz](./ctf.gz)

## Solution (CTF approach)

We have presented with a GZIP compressed file:

```
$ file ctf.gz 
ctf.gz: gzip compressed data, max compression, from Unix, original size modulo 2^32 366075035 gzip compressed data, reserved method, ASCII, has CRC, has comment, encrypted, from FAT filesystem (MS-DOS, OS/2, NT), original size modulo 2^32 366075035

$ du -hs ctf.gz 
1.4M	ctf.gz
```

We can extract it with no problem:

```
$ gunzip ctf.gz

$ du -hs ctf
350M	ctf
```

It grew 250 times, which is alarming. Actually, this file is another GZIP:

```
$ file ctf 
ctf: gzip compressed data, last modified: Wed Dec 22 20:28:53 2021, max compression, from Unix, original size modulo 2^32 532262949 gzip compressed data, reserved method, from FAT filesystem (MS-DOS, OS/2, NT), original size modulo 2^32 532262949
```

We have a GZIP bomb. I quickly realize that it is pointless to try to extract the archive in a naive way (even in memory, without using the disk space). Hexdump outputs something like this:

```
$ hexdump -C ctf
00000000  1f 8b 08 00 85 8a c3 61  02 03 ec c1 31 01 00 00  |.......a....1...|
00000010  00 c2 a0 f5 4f ed 61 0d  a0 00 00 00 00 00 00 00  |....O.a.........|
00000020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000090  00 00 00 00 00 00 00 00  6e ec c1 21 01 00 00 00  |........n..!....|
000000a0  80 a0 ff af 4d be 00 00  00 00 00 00 00 00 00 00  |....M...........|
000000b0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|

...

0fffff70  00 00 00 00 00 00 96 00  ec c1 21 01 00 00 00 80  |..........!.....|
0fffff80  a0 ff af 4d be 00 00 00  00 00 00 00 00 00 00 00  |...M............|
0fffff90  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
10000000  00 00 00 00 00 96 00 ec  c1 21 01 00 00 00 80 a0  |.........!......|
10000010  ff af 4d be 00 00 00 00  00 00 00 00 00 00 00 00  |..M.............|
10000020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|

...

15d1dbe0  00 00 00 00 00 00 00 00  00 00 00 00 96 00 ed c1  |................|
15d1dbf0  bb 09 80 30 14 00 c0 de  29 9c c3 2a 60 6b e9 02  |...0....)..*`k..|
15d1dc00  0f 51 14 7f 90 a4 13 77  77 0e e1 ee 00 00 00 00  |.Q.....ww.......|
15d1dc10  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
15d1dc70  00 00 00 00 00 00 00 fe  62 bc f7 1c b5 9d af 68  |........b......h|
15d1dc80  8f 58 f7 e8 9a a9 2e cf  90 4a ed d7 bc 95 7a a6  |.X.......J....z.|
15d1dc90  f2 36 1f e8 06 79 ec 25  b0 b9 1f                 |.6...y.%...|
15d1dc9b
```

It is clear that the challenge creators generated a bunch of these null bytes and put the flag at the very end of GZIP file.

When you play CTFs long enough, you understand that sometimes it is not required to understand how things work and decent balance between understanding and brute force is a good enough approach.

My approach was to get some bytes from the beginning, some bytes from the end, and ignore the rest. [This script](./solution.py) joins them in various combinations and generates a few thousands of smaller GZIP files in the subdirectory. One of those GZIP files decodes to a valid flag:

```
$ mkdir -p out
$ ./solution.py
$ cd out
$ for FILE in $(ls); do zcat $FILE 2>/dev/null | grep -a ctf ; done
ctf{L@stChristm@s}
```

## Solution (intended)

The proper way would be to understand the structure of GZIP file, put required bytes in the correct order and extract the flag. If you have completed that, please [let me know](https://twitter.com/oioki).
