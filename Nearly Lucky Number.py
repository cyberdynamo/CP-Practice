def luckey(n):
    if(n==0):
        return False
    while(n!=0):
        d=n%10
        if(d!=4 and d!=7):
            return False
        n=n//10
    return True
n=int(input())
temp=n
count=0
while(n!=0):
    d=n%10
    if(d==7 or d==4):
        count+=1
    n=n//10
if(luckey(count)==True):
    print("YES")
else:
    print("NO")
