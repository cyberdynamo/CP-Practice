def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

test=int(input())
for t in range(test):
    a,b=map(int,input().split())
    temp=GCD(a,b)
    print((a*b)//(temp*temp))
