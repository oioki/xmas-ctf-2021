# Day 1. First challenge

> Good Elfs with strange names (OWASP, Viris, SSRD) have hidden Santa's address. Now the new mailman is searching for a way to find Santa's valley through records and standards. Can you find the path?

## Solution

OWASP, Viris, and SSRD are the event's organizers, so the first step is to find out their domains. They are `owasp.si`, `viris.si`, and `ssrd.io`, respectively.

The challenge description mentions "mailman" and "records", so my first thought was about [MX records](https://en.wikipedia.org/wiki/MX_record). However, it turned out it was another type of DNS records - TXT. There are some interesting strings in TXT entries of organizers' domains:

```
$ dig TXT ssrd.io +short
"MS=ms97130585"
"v=spf1 include:spf.protection.outlook.com -all"
"stW0ndErFulT1"
"2ish3r3}"

$ dig TXT viris.si +short
"---- X5O!P%@AP[4PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*  ----"
"MS=03CFD10408EE8155977CFB030E239BEDA436EE2B"
"v=spf1 a:mx.viris.si include:amazonses.com ~all"
"1winter"
```

Nothing useful for `owasp.si`, though. There were no solves till this point, so later organizers released [the hint](https://twitter.com/OwaspSlovenia/status/1466013814567182336):

> Santa's do not track policy seem to be very well implemented.

After a bit of googling, we learn that DNT policy for a domain could be declared via [special URL](https://www.eff.org/dnt-policy):

```
$ curl https://xmas.owasp.si/.well-known/dnt-policy.txt
ctf{h
```

Putting all parts together, we get the flag:

```
ctf{h
1winter
2ish3r3}

ctf{h1winter2ish3r3}
```
