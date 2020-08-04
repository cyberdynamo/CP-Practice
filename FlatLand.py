import math

for t in range(int(input())):
    n=int(input())
    count=0
    while(True):
        if(n==0):
            break
        count+=1
        if(n==1):
            break
        n=n-(int(math.sqrt(n))**2)
    print(count)
