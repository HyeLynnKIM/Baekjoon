import time

count = 1234
tt=[]
for i in range(20):
    start = time.time()
    for _ in range(count):

        import sys


        def prime(x):
            if x == 1:
                return 0
            elif x <= 3:
                return 1
            elif (x % 2 == 0) | (x % 3 == 0):
                return 0
            else:
                for t in range(5, x + 1, 6):
                    if (x % t == 0) | (x % (t + 2) == 0):
                        return 1
                return 0


        a, b = map(int, sys.stdin.readline().split())
        for i in range(a, b + 1):
            if prime(i):
                print(i)


    tt.append(time.time() - start)
    print(i,"..",end=" ")
print("\n속도 >>", sum(tt)/len(tt))
#print("표준편차 : {}\tM : {}\tm : {}".format(round(numpy.std(tt),6),round(max(tt),6),round(min(tt),6)))
#[출처] [파이썬]시간초과|작성자 형우 임