import math
test=int(input())
for _ in range(test):
    n,*l=map(int,input().split())

    num1=l[0]
    num2=l[1]
    gcd=math.gcd(num1,num2)
    for i in range(2,len(l)):
        gcd=math.gcd(gcd,l[i])

    for i in range(len(l)-1):
        print(l[i]//gcd,end=" ")
    print(l[-1]//gcd)
        
