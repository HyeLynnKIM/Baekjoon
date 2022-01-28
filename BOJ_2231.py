import sys

def init(x):
    ini_list=[x]
    while(1):
        if x<10:
            ini_list.append(x)
            break
        t=x%10
        x = x // 10
        ini_list.append(t)
    return ini_list

n=int(sys.stdin.readline())
suml=[]
for i in range(1, n):
    ini=init(i)
    sum=0
    for s in ini:
        sum+=s
    if sum==n:
        suml.append(i)
    else:
        continue
if len(suml)==0:
    print(0)
else:
    print(suml[0])