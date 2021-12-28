# Day 16. Shrinking Santa's nice list

> Santa is in full preparation mode for this year's Christmas, but something unimaginable happened! One of the naughty kids sent him a USB with malware on it and now our secret server is under the attack. All we noticed is, that our list of nice kids is getting smaller and smaller every day...
> Investigate and help before more nice kids are left behind without a gift! This kind of hackers just want attention... There must be some kind of clue in the "heart" of all of this!

Files can be located at: https://we.tl/t-YbQKeIuTtK

Note: Flag is not in standard format! Submit the answer as `ctf{...}`.

## Solution

The file was quite large (726M), so it took some time to download. After the download and archive extraction, we get a larger file:

```
$ du -hs santa\'s_server.img 
3.0G	santa's_server.img

$ file santa\'s_server.img 
santa's_server.img: Linux rev 1.0 ext4 filesystem data, UUID=8772a406-f21e-40d0-8987-3bf527f25c63 (extents) (64bit) (large files) (huge files)
```

This is a dump of ext4 filesystem. So, we can mount it using special Linux loop device:

```
$ mkdir mount
$ sudo mount -o loop santa\'s_server.img mount
```

I have to say this challenge had a lot of [red herrings](https://en.wikipedia.org/wiki/Red_herring). I spent some time figuring out where to go. Here are some ways to approach the challenge:

1. The challenge description mentions "list... is getting smaller every day" and "heart". Periodic tasks in Linux are usually handled with cron daemon.

2. Most probably, organizators were preparing this challenge in the past few days. Let's try to find recently modified files (`-mtime -2` means to find files that were modified in the past 2 days, so update it with your number):

```
$ find -mtime -2 2>/dev/null
```

The output was quite big, but combining these two ideas, we discover this file:

```
$ sudo cat mount/var/spool/cron/crontabs/root
...
30 2 * * * /opt/HelpingSantasHelpers/elf.py
30 2 * * * /opt/HelpingSantasHelpers/hours.py
30 2 * * * /opt/HelpingSantasHelpers/SantasHelpers_Evaluation_Metric.py
30 2 * * * /opt/HelpingSantasHelpers/SantasHelpers_NaiveSolution.py
30 2 * * * /opt/HelpingSantasHelpers/toy.py
30 2 * * * /var/cache/private/update.py
```

The last script seems a bit off. It is obfuscated. See [update.py](./update.py) for the reference.

Skimming over this file and trying to deobfuscate, we understand that the script takes `/home/santa/NaughtyList.csv` as input, does something with it and saves something to `/var/log/apt/history.log`. This somehow aligns with the challenge description ("list of nice kids is getting smaller and smaller every day"). 

Anyway, let's look inside the [history.log](./history.log) file and watch carefully:

```
...
Start-Date: 2021-12-14  13:33:23
Commandline: /var/cache/private/update.py
Upgrade: distro-info-data:amd64 (d!$abl3_U$b_P0rts)
End-Date: 2021-12-14  13:33:23
...
```

The flag is:

```
ctf{d!$abl3_U$b_P0rts}
```

## Bonus: full deobfuscation

I wrote [this script](./deobfuscator.py) to restore the original source code of `update.py`. See [the deobfuscated code](./deobfuscated.py).

Turned out, the script is almost the exact copy of [dancing_links.py](https://github.com/RealHacker/python-gems/blob/9124eecb231ad7479fda5e21e9a9dc2639986c34/dancing_links.py). This is an algorithm to generate all possible solutions for [N-queen problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle).
