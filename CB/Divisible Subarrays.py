test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))

    bucket=[0]*n
    bucket[0]=1
    s=0
    for i in range(n):
        s+=lst[i]
        s=(s+n)%n
        bucket[s]+=1
    print(bucket)
    ans=0
    for i in range(n):
        m=bucket[i]
        ans+=(m)*(m-1)//2
    print(ans)
