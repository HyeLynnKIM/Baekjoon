import sys

a, b, c = map(int, sys.stdin.readline().split())

if c<=b:
    print(-1)
else:
    prod=int(a/(c-b))+1
    print(prod)
