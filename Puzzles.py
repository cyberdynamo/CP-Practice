n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
mini=1001
if(m==n):
    print(lst[-1]-lst[0])
else:
    for i in range(m-n+1):
        temp=lst[i+n-1]-lst[i]
        if(temp<mini):
            mini=temp
    print(mini)  
