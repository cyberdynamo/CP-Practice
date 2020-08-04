for t in range(int(input())):
    n=int(input())

    array=list(map(int,input().split()))
    bad=list(map(int,input().split()))
    dp=[0]*(n+1)
    array.append(0);bad.append(0)

    for i in range(n-1,-1,-1):
        if(array[i+1]>array[i]):
            dp[i]=dp[i+1]+1
        else:
            dp[i]=1
    ans=0
    for j in range(len(dp)-1):
        if(bad[j]!=1):
            ans+=dp[j]
    print(ans)
