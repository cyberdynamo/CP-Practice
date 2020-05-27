def fun1(num):
    if(num==1):
        return 1
    else:
        a=1
        while(a*2<=num):
            a*=2
        return a

test=int(input())
for t in range(test):
    n=int(input())
    count2=0
    while(n>0):
        count2+=1
        n-=fun1(n)
    print(count2)
