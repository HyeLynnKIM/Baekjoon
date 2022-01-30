import sys
person=[]
n=int(sys.stdin.readline())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    person.append((x, y))

cnt=1
for i in range(len((person))):
    for j in range(len(person)):
        if person[i][0]<person[j][0]:
             if person[i][1]<person[j][1]:
                 cnt+=1
    print(cnt, end=' ')
    cnt=1

