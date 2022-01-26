import sys
t=int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    if n<=h:
        print(str(n)+'01')
    else:
        sh=n//h
        re=n%h
        if re==0:
            re=h
            sh-=1
        if sh<9:
            sh+=1
            print(str(re)+'0'+str(sh))
        else:
            print(str(re)+str(sh+1))