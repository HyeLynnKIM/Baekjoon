import sys
n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
sum=[]
for i in range(0, n):
    for t in range(i+1, n):
        for j in range(t+1, n):
            s = card[i]+card[t]+card[j]
            sum.append(s)
sum.sort(reverse=True)
for s in sum:
    if s>m:
        pass
    elif s<=m:
        print(s)
        break