import sys
prime=[]
n=int(sys.stdin.readline())
if n==1:
    pass
else:
    while(n!=1):
        if n%2==0:
            print(2)
            n=n//2
            continue
        elif n%3==0:
            print(3)
            n=n//3
            continue
        else:
            for t in range(5, n+1, 6):
                if n%t==0:
                    print(t)
                    n=n//t
                    break
                elif n%(t+2)==0:
                    print(t+2)
                    n=n//(t+2)
                    break
            continue