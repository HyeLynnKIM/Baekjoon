import sys
def prime(y):
    pri=[True] * (y+1)
    maxlen = int(y ** 0.5) + 1
    for i in range(2, maxlen):
        if pri[i]:
            for j in range(i*2, y+1, i):
                pri[j]=False
    return [i for i in range(2, y+1) if pri[i]==True]
n=int(sys.stdin.readline())
for i in range(n):
    a=int(sys.stdin.readline())
    pri_list=prime(a)
    diff_list=[]
    for x in pri_list:
        diff=a-x
        if diff in pri_list:
            dlist=[x, diff, abs(diff-x)]
            diff_list.append(dlist)
    min=a
    x, y = 0, 0
    for t in diff_list:
        if min>t[2]:
            min=t[2]
            if t[0]>t[1]:
                x, y = t[1], t[0]
            else:
                x, y= t[0], t[1]
    print(x, y)
