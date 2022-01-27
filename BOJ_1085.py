import sys
x, y, w, h = map(int, sys.stdin.readline().split())
dis=[x, y, (w-x), (h-y), (x**2+y**2)**0.5, ((w-x)**2+(h-y)**2)**0.5]
dis.sort()
print(dis[0])