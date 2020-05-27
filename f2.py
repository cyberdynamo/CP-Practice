n,m,a=map(int,input().split())
tempA=n//a
tempB=m//a

if(n-(tempA*a)!=0):
    tempA+=1
if(m-(tempB*a)!=0):
    tempB+=1

print(tempA*tempB)
