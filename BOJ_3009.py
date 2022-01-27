import sys
def rm(x:list):
    if x[0]==x[1]:
        return x[2]
    elif x[1]==x[2]:
        return x[0]
    else:
        return x[1]
x=[0, 0, 0]
y=[0, 0, 0]
for i in range(3):
    x[i], y[i] = map(int, sys.stdin.readline().split())
a = rm(x)
b = rm(y)
print(a, b)