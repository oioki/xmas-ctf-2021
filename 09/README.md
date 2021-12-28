# Day 9. True secret

> Santa received ransomware from an evil elf. But his magical security reindeer team made the right decision and properly secured evidence. Can you help Santa recover the list of naughty and nice kids?

Files can be downloaded here: https://we.tl/t-nBPKrElpa0

Santa in his time machine was a little bit dizzy and left one fake flag ;)

## Solution 1 (unintended)

This challenge is about memory forensics. Initially its creators made a mistake by leaving the flag in plaintext in the memory dump:

```
$ strings dump.mem | grep 'ctf{'
cnctf{N0t_V3ry_S3cur3}
```

Due to that, the challenge was replaced with the hardened version on the next day. However, later this day I solved this challenge as intended.

## Solution 2 (intended)

We have a memory dump, and [Volatility](https://www.volatilityfoundation.org/releases) is a typical tool to use in such forensics challenges. Let's get some info about the dump:

```
$ volatility -f dump.mem imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/oioki/xmas/09/dump.mem)
                      PAE type : PAE
                           DTB : 0x185000L
                          KDBG : 0x82933be8L
          Number of Processors : 1
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0x82934c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2021-10-02 08:56:35 UTC+0000
     Image local date and time : 2021-10-02 10:56:35 +0200
```

The most important is profile (`Win7SP1x86_23418`) which we have to specify in the subsequent volatility runs. The challenge called `True secret` and contains the file with the same name, so likely we are dealing with [TrueCrypt](https://en.wikipedia.org/wiki/TrueCrypt) encrypted file. We can get the TrueCrypt binary [here](https://sourceforge.net/projects/truecrypt/files/TrueCrypt/Other/TrueCrypt-7.2-Linux-console-x64.tar.gz/download).

Let's try to find the password in the memory, using the `truecryptsummary` volatility plugin:

```
$ volatility -f dump.mem --profile=Win7SP1x86_23418 truecryptsummary
Volatility Foundation Volatility Framework 2.6.1
Registry Version     TrueCrypt Version 7.1a
Password             geslo123 at offset 0x8e701064
Process              TrueCrypt.exe at 0x83f48030 pid 524
Service              truecrypt state SERVICE_RUNNING
Kernel Module        truecrypt.sys at 0x8e6cd000 - 0x8e704000
Symbolic Link        E: -> \Device\TrueCryptVolumeE mounted 2021-10-02 08:56:11 UTC+0000
Symbolic Link        Volume{f55120a6-235d-11ec-adde-20791829acf1} -> \Device\TrueCryptVolumeE mounted 2021-10-02 08:56:11 UTC+0000
Symbolic Link        E: -> \Device\TrueCryptVolumeE mounted 2021-10-02 08:56:11 UTC+0000
File Object          \Device\TrueCryptVolumeE\ at 0x172f0f80
File Object          \Device\TrueCryptVolumeE\ at 0x1e03f340
Driver               \Driver\truecrypt at 0x1eb337a8 range 0x8e6cd000 - 0x8e703b80
Device               TrueCryptVolumeE at 0x83ef7a38 type FILE_DEVICE_DISK
Container            Path: \??\C:\Users\Tasha\Documents\MySecrets
Device               TrueCrypt at 0x85133ca8 type FILE_DEVICE_UNKNOWN
```

The password is `geslo123` ("geslo" is "password" in Slovenian).

Indeed, it is our password for the TrueCrypt disk image (which was also provided):

```
$ ./truecrypt TrueSecret mount
```

The mounted disk contains only a single file with the link to [pastebin](https://pastebin.com/FX6CmRSA). Its contents were `2PN4XQGdPo31Fb5MCAmECmRUGqPz`. It is not Base64, but something else. When I get tired of this guessing, I just use [CyberChef Magic method](https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')&input=MlBONFhRR2RQbzMxRmI1TUNBbUVDbVJVR3FQeg). Just to double check:

```
$ base58 -d
2PN4XQGdPo31Fb5MCAmECmRUGqPz
ctf{N0t_V3ry_S3cur3}
```

## Solution 3 (hardened version)

I could not identify the correct profile of the new image with my volatility version, so I used [volatility Docker image](https://hub.docker.com/r/phocean/volatility) with the recent profiles available:

```
$ function volatility() {   docker run --rm --user=$(id -u):$(id -g) -v "$(pwd)":/dumps:rw,Z -ti phocean/volatility $@; }

$ volatility -f /dumps/dump.mem imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win10x64_19041
                     AS Layer1 : SkipDuplicatesAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/dumps/dump.mem)
                      PAE type : No PAE
                           DTB : 0x1ad002L
                          KDBG : 0xf8016fe1db20L
          Number of Processors : 2
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0xfffff8016e0eb000L
                KPCR for CPU 1 : 0xffffdb005e9c0000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2021-12-10 06:45:00 UTC+0000
     Image local date and time : 2021-12-10 07:45:00 +0100
```

We can do some other stuff, like dumping process list (see [pslist.txt](./pslist.txt)):

```
$ volatility --profile Win10x64_19041 -f /dumps/dump.mem pslist > pslist.txt
```

However, doing some other stuff resulted in a weird error. This is probably due to my setup, but whatever:

```
$ volatility --profile Win10x64_19041 -f /dumps/dump.mem clipboard
Volatility Foundation Volatility Framework 2.6.1
Session    WindowStation Format                         Handle Object             Data                                              
---------- ------------- ------------------ ------------------ ------------------ --------------------------------------------------
WARNING : volatility.debug    : Cannot find nt!ObGetObjectType
WARNING : volatility.debug    : Cannot find nt!ObGetObjectType
Traceback (most recent call last):
  File "vol.py", line 192, in <module>
    main()
  File "vol.py", line 183, in main
    command.execute()
  File "/volatility/volatility/commands.py", line 147, in execute
    func(outfd, data)
  File "/volatility/volatility/plugins/gui/clipboard.py", line 155, in render_text
    for session, wndsta, clip, handle in data:
  File "/volatility/volatility/plugins/gui/clipboard.py", line 66, in calculate
    for wndsta in windowstations.WndScan(self._config).calculate():
  File "/volatility/volatility/plugins/gui/windowstations.py", line 57, in calculate
    for wind in self.scan_results(addr_space):
  File "/volatility/volatility/poolscan.py", line 252, in scan
    skip_type_check = skip_type_check)
  File "/volatility/volatility/plugins/overlays/windows/windows.py", line 1258, in get_object
    return self.get_object_top_down(struct_name, object_type, skip_type_check)
  File "/volatility/volatility/plugins/overlays/windows/windows.py", line 1231, in get_object_top_down
    header.get_object_type() == object_type):
  File "/volatility/volatility/plugins/overlays/windows/win7.py", line 155, in get_object_type
    return self.type_map.get(int(self.TypeIndex), '')
  File "/volatility/volatility/plugins/overlays/windows/win10.py", line 334, in TypeIndex
    return ((addr >> 8) ^ cook ^ indx) & 0xFF
TypeError: unsupported operand type(s) for ^: 'int' and 'NoneType'
```

I noticed that one of the processes were `notepad.exe`, and volatility challenges creators love to put some sensitive into Notepad documents. Let's extract some strings from there:

```
$ volatility --profile Win10x64_19041 -f /dumps/dump.mem memdump -p 6148 -D /dumps/memdump/
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing notepad.exe [  6148] to 6148.dmp

$ strings 6148.dmp > 6148.dmp.str
```
 
and expect the password to be in some readable form (like `geslo123` but add a few special characters just to make sure):

```
$ grep -E '^[a-z0-9!@#$%^&*()_]{1,39}$' 6148.dmp.str | sort | uniq > 6148.dmp.str2
```

This is where I am not proud of myself, because I had to use a tool to bruteforce the TrueCrypt password:

```
$ git clone https://github.com/lvaccaro/truecrack
$ cd truecrack
$ ./configure --enable-cpu
$ make

$ bin/truecrack -v -t gg.tc -w memdump/6148.dmp.str2
TrueCrack v3.6
Website: http://code.google.com/p/truecrack
Contact us: infotruecrack@gmail.com

Memory initialization...

COUNT	PASSWORD	RESULT
0	!!!!		NO
1	!!!%		NO
...
956	0948d		NO
957	!095		NO
958	)098)		NO
959	098f6bcd4621d373cade4e832627b4f6	YES
Found password:		"098f6bcd4621d373cade4e832627b4f6"
Password length:	"33"
Total computations:	"960"
```

The correct password is `098f6bcd4621d373cade4e832627b4f6` (by the way, this is an MD5 hash for `test` string).

Let's do the same as in Solution 2:

```
$ ./truecrypt gg.tc mount
```

The image contains a single file:

```
$ base58 -d mount/secretdata.txt 
https://pastebin.com/N9kHEfZW
```

And we get the flag by visiting https://pastebin.com/N9kHEfZW:

```
ctf{All1Want4XmassIsY0u}
```

## Solution 4 (hardened version, intended)

Do you know the proper solution? Please [let me know](https://twitter.com/oioki).
