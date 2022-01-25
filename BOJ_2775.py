import sys

def room(k, n):
  if n==1:
    return 1
  elif k==0:
    return n
  return room(k-1, n)+room(k, n-1)

a = int(sys.stdin.readline())
for i in range(a):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())
  print(room(k, n))