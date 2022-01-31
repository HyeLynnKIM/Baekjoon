import sys
from copy import deepcopy
tmp=[]
change=[]
def black(chess1, a, b):
    ## 1) start is 'B' down
    cur='B'
    chg=0
    for i in range(8):
        for j in range(8):
            if j==0:
                if ((a+i) % 2) == 1: cur = 'W'
                else: cur = 'B'
            if chess1[a+i][b+j] != cur:
                chess1[a+i][b+j] = cur
                chg+=1
            if cur == 'B': cur = 'W'
            else: cur = 'B'
    change.append(chg)
def white(chess2, a, b):
    ## 2) start is 'W'
    cur='W'
    chg = 0
    for i in range(8):
        for j in range(8):
            if j==0:
                if ((a+i) % 2) == 0: cur = 'W'
                else: cur = 'B'
            if chess2[a+i][b+j] != cur:
                chess2[a+i][b+j] = cur
                chg += 1
            if cur == 'B': cur = 'W'
            else: cur = 'B'
    change.append(chg)
chess=[]
x, y = map(int, sys.stdin.readline().split())
for i in range(x):
    line = str(sys.stdin.readline())
    tmp.append(line)
tmp = [line.rstrip() for line in tmp]
for i in range(x):
    line = list(tmp[i])
    chess.append(line)
for i in range(x-7):
    for j in range(y-7):
        c1=deepcopy(chess)
        c2=deepcopy(chess)
        black(c1, i, j)
        white(c2, i, j)
change.sort()
print(change[0])