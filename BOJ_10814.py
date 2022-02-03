import sys
n=int(sys.stdin.readline())
cnt=[]
for _ in range(n):
    cnt.append(list((sys.stdin.readline().split())))
cnt=sorted(cnt, key=lambda x:(int(x[0])))
for i in range(n):
    print(cnt[i][0], cnt[i][1])