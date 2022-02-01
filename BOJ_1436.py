import sys
n=int(sys.stdin.readline())
cnt=0
s=666
while(1):
    for i in range(0,(len(str(s)))-2):
        if str(s)[i:i+3]=='666':
            cnt+=1
            break
    if cnt==n:
        print(s)
        break
    s+=1

## 6000대일때 10개씩하고 나머지는 1개씩방식도 좀 더 빠를듯
