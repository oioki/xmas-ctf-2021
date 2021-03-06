# Day 7. Letter to Santa

> Santa got a Christmas letter in some esoteric language. Please help Santa to read this:

```
????????????(????????)??????!(!)?????????(???????????)?????????!(!)?????????????(???????)??????!(!)???????????(?????????)????!(!)?????????????(?????????)??????!(!)?????????(???????????)??!(!)???????????(??????????)?????!(!)???(?????????????)?????????!(!)??????????(??????????)????????!(!)???????????????????(?????)??!(!)??????????????????????(?????)!(!)?????????????????(??????)?!(!)???????(????????????)?!(!)????????(???????????)?????????!(!)????????(????????????)???????!(!)??????????(?????)?!(!)?????????????(???????)????!(!)????????(????????????)??????!(!)????????????(?????????)????????!(!)???????????????????(??????)?????!(!)???(?????????)??????!(!)??????(?????)???!(!)???(?????????)??????!(!)?????????(?????????????)????????!(!)
```

IMPORTANT: The flag for this challenge is not in the standard competition format.

## Solution

I quickly realized that it is relatively hard to Google the name of this esoteric language, because the program consists only from punctuation characters which Google treats specially. However, I landed on this [list of esoteric languages](https://esolangs.org/wiki/Language_list). Skimming over the list, I found the right language - [(?!)](https://esolangs.org/wiki/(%3F!)).

It was also hard to find the interpreter for this language, so I wrote my own [decoder](./solution.py):

```
$ ./solution.py
flag{es0langUag3_ftw!!!}
```
