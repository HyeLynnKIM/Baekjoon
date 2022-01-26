import sys
sys.setrecursionlimit(10**6)
def spaceship(dis, vel):
    cnt=2
    dis=dis-2*vel
    if dis<=(vel+1):
        cnt+=1
    elif dis<=2*(vel+1):
        cnt+=2
    else:
        cnt+=spaceship(dis, vel+1)
    return cnt
t = int(sys.stdin.readline())
for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    if y-x==1:
        print(1)
    elif y-x==1:
        print(2)
    else:
        print(spaceship((y-x),1))