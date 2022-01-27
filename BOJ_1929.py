import sys
def prime(y):
    pri=[True] * (y+1)
    maxlen=int(y**0.5)+1
    for i in range(2, maxlen):
        if pri[i]:
            for j in range(2*i, y+1, i):
                pri[j]=False
    return [i for i in range(a, len(pri)) if pri[i]==True]
a, b = map(int, sys.stdin.readline().split())
pri_list = prime(b)
for x in pri_list:
    if x==1:
        pass
    elif x>=a:
        print(x)
