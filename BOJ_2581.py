import sys

n1=int(sys.stdin.readline())
n2=int(sys.stdin.readline())
prime=[]
for i in range(n1, n2+1):
    if i!=1:
        prime.append(i)
        for t in range(2, i):
            if i%t==0:
                prime.remove(i)
                break
sum=0
for nu in prime:
    sum+=nu
if len(prime)==0:
    print(-1)
else:
    print(sum)
    print(prime[0])