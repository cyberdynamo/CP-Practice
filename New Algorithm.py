n,a=map(int,input().split())
while(a!=0):
    d=n%10
    if(d==0):
        n//=10
    else:
        n-=1
    a-=1
print(n)
