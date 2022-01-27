import sys
n=int(sys.stdin.readline())
f1, f2 = 0, 1
fn=0
if n==0: print(0)
elif n==1: print(1)
else:
    for i in range(n-1):
        fn=f1+f2
        f1=f2
        f2=fn
    print(fn)