test=int(input())
for t in range(test):
    a,b,c=map(int,input().split())
    mini=(10**9+7)
    for i in range(a+1):
        j=a-i
        s=b*(i**2)+c*(j**2)
        if(s<mini):
            mini=s
    print(mini)
