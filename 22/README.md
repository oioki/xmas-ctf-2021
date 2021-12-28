# Day 22. Another encrypted message

> Santa received this from reindeers. Are they ok? Is something wrong?

```
D2 B L' U2 L2 F R' U F B' B2 L2 B B' U L2 F' L' R R2 D

R2 L R' F2 D' L R F' R2 B' F D2 D2 L' B D R B F' L' F2

B' B' R2 F' R L D2 B F2 L' L R U F' F B' R2 D' L' B R R2 L2 U U R' F2 R R2 B F R2 D R R2 L U2 U' U' U'
```

## Solution

If you're even a bit familiar with math and logic puzzles, you could almost immediately recognize [Rubik's Cube notation](https://ruwix.com/the-rubiks-cube/notation/). Likely, the challenge is about steganography using the Rubik's Cube.

There are [quite](https://epublications.regis.edu/cgi/viewcontent.cgi?article=1511&context=theses) [a few](https://scialert.net/fulltext/?doi=rjit.2013.329.340) [papers](https://informatika.stei.itb.ac.id/~rinaldi.munir/Penelitian/Makalah-ITES-2018.pdf) involving Rubik's Cube as a method of encryption/steganography and a bunch of CTF solutions based on them.

Let's download all of these past solutions somewhere and go back to our challenge. There are three sequences. The number of steps in each line is 21, 21, 40, respectively. This fact is a huge hint towards [this solution](https://gist.github.com/nbulischeck/0906e7c75459ffad3141e5c224e383bc) where the number of steps was 21, 21, 80. However, when we try to run the magic script with our custom values for `CHALL_PHDR`, `CHALL_LHDR`, `CHALL_MSG`, it does not produce anything meaningful:

```
$ ./rubikstega.py
Xgw±F
```

Let's look again at the challenge description: "Are they ok? Is something wrong?" This might be a pointer that the algorithm is right, but something might be slightly off. After few hours of failed attempts, I found the fix:

```
#length = get_length(enc_table, CHALL_LHDR)
length = get_length(enc_table, CHALL_LHDR) + 1
```

See the [rubikstega.py](./rubikstega.py). Apparently, reindeers made a typical off-by-one error:

```
$ ./rubikstega.py
ctf{GoodT0Go
```
