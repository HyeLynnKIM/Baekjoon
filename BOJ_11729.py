import sys

def hanoi(n, x, y, z):
    if n==1:
        print(x,z)
        return
    hanoi(n-1, x, z, y)
    print(x,z)
    hanoi(n-1, y, x, z)

n=int(sys.stdin.readline())
print((2**n)-1) ## how we can do when we don't know cnt
hanoi(n, 1, 2, 3)
