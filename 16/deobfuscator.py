#!/usr/bin/env python3

f = open('update.py', 'r')
lines = f.readlines()
f.close()

for line in lines:
    line = line[:-1].replace('\t', '    ')
    if '#line' not in line:
        print(line)
        continue

    parts = line.split('#line:')

    spaces = len(parts[0]) - len(parts[0].lstrip(' '))
    print(' ' * spaces, end='')

    original_line = ':'.join(parts[1].split(':')[1:])
    print(original_line)
