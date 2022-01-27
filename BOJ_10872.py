import sys
n=int(sys.stdin.readline())
sum=1
for i in range(2, n+1):
    sum*=i
print(sum)