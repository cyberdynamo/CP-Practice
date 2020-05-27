def mini(a):
    mini=10000000000000001
    while(a):
        temp=a%10
        if(temp<mini):
            mini=temp
        a=a//10
    return mini
 
def maxi(a):
    maxi=0
    while(a):
        temp=a%10
        if(temp>maxi):
            maxi=temp
        a=a//10
    return maxi 
 
 
test=int(input())
for t in range(test):
    a,k=map(int,input().split())
    if(k==1):
        print(a)
    else:
        for i in range(k-1):
            if(mini(a)==0):
                break
            a=a+(mini(a)*maxi(a))
        print(a)
