import sys
n=int(sys.stdin.readline())
num=[]
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
for nu in num:
    print(nu)