# Day 4. Shiny Bubbles

> One of Santa's elf found this image of shiny bubbles. They are hiding a deep secret that you just have to "print" out.

[shiny_bubbles.zip](./shiny_bubbles.zip)

## Solution

There is a `shiny_bubbles.png` image inside, but you cannot extract it right away -- the archive is password-protected. One direct way to approach this is to brute-force the password, using `fcrackzip` tool and a decent word list. [rockyou.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz) is one such good enough and [famous](https://www.cosmodiumcs.com/post/the-story-of-rockyou) wordlist.

Bruteforcing the password:

```
$ fcrackzip -u -v -D -p rockyou.txt shiny_bubbles.zip 
found file 'shiny_bubbles.png', (size cp/uc 1943050/2210609, flags 1, chk d877)

PASSWORD FOUND!!!!: pw == 4everspunkybubbles
```

Extract image from the archive:
![shiny_bubbles.png](./shiny_bubbles.png)

Nothing unusual in the image itself, so let's look at the bytes. Quick hit - let's grep for `ctf` which is our flag format:

```
$ strings shiny_bubbles.png  | grep ctf
1/1ctf{Wrong_Flag_Keep_Searching}PK
10/10ctf{Wrong_Flag_Keep_Searching}PK
100/100ctf{Wrong_Flag_Keep_Searching}PK
101/101ctf{Wrong_Flag_Keep_Searching}PK
102/102ctf{Wrong_Flag_Keep_Searching}PK
103/103ctf{Wrong_Flag_Keep_Searching}PK
104/104ctf{Wrong_Flag_Keep_Searching}PK
...
```

Okay, we're on a good path. Let's filter out "Wrong":

```
$ strings shiny_bubbles.png  | grep ctf | grep -v Wrong
718/718ctf{th1s_I5_fuN_GREP_r0ck5}
```
