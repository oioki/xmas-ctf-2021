# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.12 (default, Sep 10 2021, 00:20:04) 
# [GCC 9.3.0]
# Embedded file name: SuperEasy.py
# Compiled at: 2021-11-14 10:39:27
# Size of source mod 2**32: 1447 bytes


def head(passwd):
    head_status = 0
    if passwd[:4] == 'ctf{':
        head_status = 1
    return head_status


def tail(passwd):
    tail_status = 0
    if passwd[25] == '}':
        tail_status = 1
    return tail_status


def center1(passwd):
    center1_status = 0
    if passwd[12] == 's':
        if passwd[8] == 'r':
            if passwd[7] == '3':
                if passwd[22] == 'Y':
                    if passwd[21] == sep:
                        center1_status = 1
    if passwd[15] == 'K':
        if passwd[16] == passwd[19]:
            if passwd[23] == 'u':
                if passwd[19] == '3':
                    center1_status = 1
    return center1_status


def center2(passwd):
    center2_status = 0
    if passwd[23] == 'u':
        if passwd[17] == 'y':
            if passwd[9] == sep:
                if passwd[4] == 'S':
                    if passwd[11] == '4':
                        center2_status = 1
    if passwd[19] == passwd[7]:
        if passwd[14] == sep:
            if passwd[5] == 'u':
                if passwd[13] == passwd[22]:
                    if passwd[24] == '5':
                        center2_status = 1
    return center2_status


def center3(passwd):
    center3_status = 0
    if passwd[18] == 'G':
        if passwd[13] == 'Y':
            if passwd[24] == '5':
                if passwd[10] == 'e':
                    if passwd[6] == 'p':
                        center3_status = 1
    if passwd[20] == 'n':
        if passwd[14] == sep:
            if passwd[15] == 'k':
                center3_status = 1
    return center3_status


sep = '_'
passwd_in = input('Enter flag: ')
if head(passwd_in) == 1and center1(passwd_in) == 1and center2(passwd_in) == 1 and center1(passwd_in) == 1 and tail(passwd_in) == 1:
    print('Great job!')
else:
    print('Nope, try again.')
# okay decompiling SuperEasy.pyc
