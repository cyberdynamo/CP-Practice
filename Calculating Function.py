n=int(input())
m=n
s=0
flag=0
if(n%2==0):
    n-=1
    flag=1
temp=n-1
c1=temp//2
if(c1%2==0):
    s+=(-(n//2+1))
else:
    s+=(-1-n)
    s+=(n//2+1)
if(flag==1):
    s+=(m)
print(s)
