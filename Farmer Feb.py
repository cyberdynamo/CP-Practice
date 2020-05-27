def checkprime(a):
    flag=0
    for i in range(2,a//2+1):
        if(a%i==0):
            flag=1
            break
    if(flag==1):
        return False
    else:
        return True
    
def Fun(a):
    while(True):
        if(checkprime(a)==True):
            return a
        else:
            a+=1
        
test=int(input())
for t in range(test):
    n,m=map(int,input().split())
    s=n+m
    print(Fun(s+1)-s)
