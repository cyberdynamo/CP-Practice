test=int(input())
for t in range(test):
    n=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))

    lst1.append(0)
    lst2.append(0)
    dp=[0]*(n+1)

    for i in range(n-1,-1,-1):
        if(lst1[i+1]>lst1[i]):
            dp[i]=dp[i+1]+1
        else:
            dp[i]=1
    s=0
    for i in range(n):
        if(lst2[i]!=1):
            s+=dp[i]
    print(s)
