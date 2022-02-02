import sys
import statistics
from collections import Counter # factor count

n=int(sys.stdin.readline())
cnt=[int(sys.stdin.readline()) for _ in range(n)]
C = sorted(Counter(cnt).items(), key=lambda x: (-x[1], x[0]))

print(round(statistics.mean(cnt)))
print(statistics.median(cnt))
maximum=1
m=[]
for i in C:
    if i[1]>maximum:
        del m[:]
        maximum=i[1]
        m.append(i[0])
    elif i[1]==maximum:
        m.append(i[0])
try: print(m[1])
except: print(m[0])
print(max(cnt)-min(cnt))