#!/usr/bin/env python3

data = open('SnakeData.txt', 'r').read()
data = data.split(',')



# https://theasciicode.com.ar/extended-ascii-code/block-graphic-character-ascii-code-219.html

s = []

for i in range(25):
    s.append(['.'] * 25)

def dump():
  for i in range(25):
    for j in range(25):
        if s[i][j] == '1':
            print('█', end='')
        else:
            print(' ', end='')
#            print(s[i][j], end='')
    print()
  print()


#print(data)

#print(len(data))

cnt = 0

def aaa():
    if data[cnt] == '1':
        print('#', end='')
    else:
        print(' ', end='')


def draw(L, offX, offY):
  global cnt

  l = 25
  l = L

  for i in range(l):
    s[offX + 0][offY + i] = data[cnt]
    cnt += 1


  l = 24
  l = L-1

  for i in range(l):
    s[offX + i+1][offY + L-1] = data[cnt]
    cnt += 1


  l = 24
  l = L-1

  for i in range(l):
    s[offX + L-1][offY + L-2-i] = data[cnt]
    cnt += 1

  l = 23
  l = L-2

  for i in range(l):
    s[offX + L-2-i][offY + 0] = data[cnt]
    cnt += 1


draw(25, 0, 0)
draw(23, 1, 1)
draw(21, 2, 2)
draw(19, 3, 3)
draw(17, 4, 4)
draw(15, 5, 5)
draw(13, 6, 6)
draw(11, 7, 7)
draw(9, 8, 8)
draw(7, 9, 9)
draw(5, 10, 10)
draw(3, 11, 11)

dump()
