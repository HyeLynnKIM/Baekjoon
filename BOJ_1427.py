import sys
s=str(sys.stdin.readline())
string=list(s)
string.sort(reverse=True)
for t in string:
    print(t, end='')