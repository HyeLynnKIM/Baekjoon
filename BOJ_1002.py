import sys
n=int(sys.stdin.readline())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    middis=(((x2-x1)**2+(y2-y1)**2))**0.5
    rsum=r1+r2
    rdiff=abs(r1-r2) ## I don't think of this part...
    if (x1==x2) and (y1==y2) and (r1==r2):
        print(-1)
    elif ((x1==x2) and (y1==y2)) or (middis<rdiff) or (middis>rsum):
        print(0)
    elif middis==rsum or middis==rdiff:
        print(1)
    elif middis<rsum or middis>rdiff:
        print(2)