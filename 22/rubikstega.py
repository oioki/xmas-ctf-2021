#!/usr/bin/env python3

# Values from the white paper
EXAMPLE_PHDR = 'L2 F\' B2 U D2 B U D\' F2 L\' F U2 R U\' L\' R\' U\' B F D U\''.split(" ")
EXAMPLE_LHDR = 'B U2 D2 R\' F U2 B R L\' B L\' B L\' D F\' L U\' B2 R F2 L\' F2'.split(" ")
EXAMPLE_MSG = 'F L U2 L2 F\' B D\' B2 L\' B\' U L2 F\' R2 D\' B\' U\' L\' B R D2 L2 R\' B F2 D\' U R B D2 U2 R2 U\' F2 R2 F D F2 B2 D\' R\' D R\' U\' F\' B2 U F2 D R U L F U2 L2 D R B D\' B\' U L U\''.split(" ")

# Values from the challenge
#CHALL_PHDR = 'B2 R U F\' R\' L\' B B2 L F D D\' R\' F2 D\' R R D2 B\' L R'.split(" ")
#CHALL_LHDR = 'L\' L B F2 R2 F2 R\' L F\' B\' R D\' D\' F U2 B\' U U D\' U2 F\''.split(" ")
#CHALL_MSG = 'L F\' F2 R B R R F2 F\' R2 D F\' U L U\' U\' U F D F2 U R U\' F U B2 B U2 D B F2 D2 L2 L2 B\' F\' D\' L2 D U2 U2 D2 U B\' F D R2 U2 R\' B\' F2 D\' D B\' U B\' D B\' F\' U\' R U U\' L\' L\' U2 F2 R R F L2 B2 L2 B B\' D R R\' U L'.split(" ")

CHALL_PHDR = "D2 B L' U2 L2 F R' U F B' B2 L2 B B' U L2 F' L' R R2 D".split(" ")
CHALL_LHDR = "R2 L R' F2 D' L R F' R2 B' F D2 D2 L' B D R B F' L' F2".split(" ")
CHALL_MSG  = "B' B' R2 F' R L D2 B F2 L' L R U F' F B' R2 D' L' B R R2 L2 U U R' F2 R R2 B F R2 D R R2 L U2 U' U' U'".split(" ")

notation1 = ["D", "B'", "L", "R'", "R", "L'", "F2", "U", "B2"]
notation2 = ["R2", "D'", "F", "U'", "B", "F'", "U2", "L2", "D2"]

default_table = [
    [0, "L", "F"],
    [1, "R", "B"],
    [2, "U", "L2"],
    [3, "D", "R2"],
    [4, "F2", "U2"],
    [5, "B2", "D2"],
    [6, "L'", "F'"],
    [7, "R'", "U'"],
    [8, "B'", "D'"],
]

def find_encoded(i, seq):
    if i in notation1:
        f = lambda x: x[2] == i
    elif i in notation2:
        f = lambda x: x[3] == i
    else:
        quit(0)

    for item in seq:
        if f(item): 
            return item[1]

def find_default(i, seq):
    if i in notation1:
        f = lambda x: x[1] == i
    elif i in notation2:
        f = lambda x: x[2] == i
    else:
        quit(0)

    for item in seq:
        if f(item): 
            return item[0]

def get_enc_table(HEADER):
    # Step 1: Map header to default table in base-9
    ENCODED_P = ''.join([str(find_default(i, default_table)) for i in HEADER])

    # Step 2: Convert first scramble into decimal
    ENCODED_P = str(int(ENCODED_P, 9))

    # Reverse engineering of 2.1.1 Embedding the permutation information
    i = int(ENCODED_P[0])
    sub1 = ENCODED_P[1:i+1]
    P = ENCODED_P[i+1:i+10]
    sub2 = ENCODED_P[i+10:]

    # Use P to permute the default encoding table
    enc_table = [default_table[int(x)] for x in P]

    # Insert the "After" indexes
    for idx, item in enumerate(enc_table):
        item.insert(1, idx)

    return enc_table

def get_length(enc_table, HEADER):
    # Step 1: Map header to encoded table in base-9
    HEADER_LENGTH = ''.join([str(find_encoded(i, enc_table)) for i in HEADER])

    # Step 2: Convert first scramble into decimal
    HEADER_LENGTH = str(int(HEADER_LENGTH, 9))

    # Reverse engineering of 2.1.3 Embedding the length information
    j = int(HEADER_LENGTH[0])
    k = int(HEADER_LENGTH[1])
    sub3 = HEADER_LENGTH[2:j+2]
    length = int(HEADER_LENGTH[j+2:j+2+k])
    sub4 = HEADER_LENGTH[j+2+k:]

    return length

def decrypt_message(length, enc_table, MESSAGE):
    # Step 1: Get m by taking length notations starting from third scramble
    MESSAGE_PIECE = MESSAGE[0:length]

    # Step 2: Map header to encoded table in base-9
    MAPPED_MESSAGE = ''.join([str(find_encoded(i, enc_table)) for i in MESSAGE_PIECE])

    # Step 2: Convert first scramble into decimal, then binary
    MAPPED_MESSAGE = int(MAPPED_MESSAGE, 9)
    BINARY_MESSAGE = f"{MAPPED_MESSAGE:b}"

    # Step N: Pad
    PADDED_MESSAGE = '0' * (8 - (151 % 8)) + BINARY_MESSAGE

    # Step N: Chunk
    CHUNKED_MESSAGE = [PADDED_MESSAGE[i:i+8] for i in range(0, len(PADDED_MESSAGE), 8)]

    # Step N: Join
    DECRYPTED_MESSAGE = ''.join([chr(int(x, 2)) for x in CHUNKED_MESSAGE])

    print(DECRYPTED_MESSAGE)

enc_table = get_enc_table(CHALL_PHDR)
#length = get_length(enc_table, CHALL_LHDR)
length = get_length(enc_table, CHALL_LHDR) + 1
decrypt_message(length, enc_table, CHALL_MSG)
