import sys
n=int(sys.stdin.readline())
cnt=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt=sorted(cnt, key=lambda x: (x[1], x[0]))
for t in cnt:
    print(t[0], t[1])