import sys

n=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))
prime=[] ## remove하면 index꼬임
for nu in num:
    if nu!=1:
        prime.append(nu)
        for i in range(2,nu):
            if nu%i==0:
                prime.remove(nu)
                break
print(len(prime))