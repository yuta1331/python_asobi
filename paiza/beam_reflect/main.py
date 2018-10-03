# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# 2d array = vertical and horizontal

R = [0, 1] # right
L = [0, -1] # left
U = [-1, 0] # up
B = [1, 0] # bottom

H = 0 # height
W = 1 # width

# posision: 2d array 
# direction: 2d array
def MovedP(pos, dire, HnW):
    for i in range(2):
        tmp = pos[i] + dire[i]
        if tmp >= 0 and tmp < HnW[i]:
            pos[i] = tmp
        else:
            return 0
    return pos

def JudgedD(pos, dire, mirr):
    if mirr[pos[H]][pos[W]] == '/':
        tmp = dire[H]
        dire[H] = -dire[W]
        dire[W] = -tmp
    elif mirr[pos[H]][pos[W]] == '\\':
        tmp = dire[H]
        dire[H] = dire[W]
        dire[W] = tmp
    return dire

# main

def main():
    HnW = list(map(int, input().split()))
    mirror = ['' for i in range(HnW[H])]
    for i in range(HnW[H]):
        mirror[i] = input()
    Dir = R # init direction
    Pos = [0, 0] # init position
    count = 0
    
    while(1):
        Pos = MovedP(Pos, Dir, HnW)
        count += 1
        if Pos == 0:
            print(count)
            return
        Dir = JudgedD(Pos, Dir, mirror)

main()
