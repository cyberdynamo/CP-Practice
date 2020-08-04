import math
for test in range(int(input())):
    n=int(input())
    m=str(bin(n))[2:]
    s=n
    n+=1
    l=len(m)
    i=1
    while(l!=1):
        print(l)
        s+=(math.ceil(n//(2**i)))
        i*=2
        l-=1
    print(s)
