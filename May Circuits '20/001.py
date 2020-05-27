def fact(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return fact
    
a,b=map(int,input().split())
if(b>5):
    f=0
else:
    f=fact(b)%10
    
if(a!=0):
    temp=a**f
    print(temp%10)
else:
    print(0)
