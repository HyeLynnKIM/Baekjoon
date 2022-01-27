import sys
while(1):
    side = list(map(int, sys.stdin.readline().split()))
    if 0 in side:
        break
    side.sort(reverse=True)
    if((side[0]**2) == ((side[1]**2)+(side[2]**2))):
        print("right")
    else:
        print("wrong")