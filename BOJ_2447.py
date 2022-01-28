## hard...
import sys
def star(x):
    if x==3:
        return ['***', '* *', '***']
    stars = star(x//3)
    arr=[]
    for st in stars:
        arr.append(st*3)
    for st in stars:
        arr.append(st+ ' '*(x//3)+st)
    for st in stars:
        arr.append(st*3)
    return arr

n=int(sys.stdin.readline())
print('\n'.join(star(n)))