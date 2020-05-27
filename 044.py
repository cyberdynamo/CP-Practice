import math
test=int(input())
for _ in range(test):
    n=int(input())
    lst=[]
    lst.append(n)
    while(n!=1):
        if(n%2==0):
            n=math.sqrt(n)
            n=int(n)
        else:
            n=n*(math.sqrt(n))
            n=int(n)

        lst.append(n)

    for j in range(len(lst)-1):
        print(lst[j],end=" ")
    print(lst[-1])
