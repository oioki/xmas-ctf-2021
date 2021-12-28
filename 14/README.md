# Day 14. QR Snake

> This spiral just turned flat... You are reversing master right?

[SnakeData.txt](./SnakeData.txt)

## Solution

If you combine the challenge name and the fact that "spiral just turned flat", you can come to the idea that the challenge was created from the QR code which was cut into spiral and then converted to a sequence of numbers ("snake").

It is more a programming challenge than CTF. It's a matter of time to write the program. Here is [my solution](./solution.py):

```
$ ./solution.py
███████ █  ████ █ ███████
█     █  ██  ██ █ █     █
█ ███ █   █ ███   █ ███ █
█ ███ █     ██ █  █ ███ █
█ ███ █  █ █   ██ █ ███ █
█     █   █ ██    █     █
███████ █ █ █ █ █ ███████
        █ ██ █  █        
██ ██ █  ████████ █     █
██ ██    █  ██ █ ██████  
█ █  ██   ██ █ █ ███ ██ █
██ ██   ████  █   ███████
 █ ██ ██ █     ██ █ █   █
█  █ █     █ ██████ █ ██ 
██   ████ █ ██ ██ █ █  ██
█ ███  ███      █   █ ██ 
█ ██ ██  ████  ██████ ███
        █   █████   ████ 
███████  █ ██   █ █ █   █
█     █   █  █  █   ██ █ 
█ ███ █ ██  ██████████   
█ ███ █ █ ██████ ███   ██
█ ███ █   ██   █  ████ ██
█     █ █ █ █ █    █  ███
███████ █ ██  █ █  ███  █
```

Terminal font usually has a higher height-to-width ratio. So open your favorite QR code reader and tilt the mobile phone over the screen to get the flag:

```
ctf{7h!s_QR_c0de_!s_a_M3$$}
```
