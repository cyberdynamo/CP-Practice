test=int(input())
for t in range(test):
    n=int(input())
    for k in range(n):
        I,N,Q=map(int,input().split())
        ans=0
        if(I==1):
            if(N%2!=0):
                if(Q==1):
                    ans=N//2
                else:
                    ans=N//2+1
            else:
                ans=N//2
        else:
            if(N%2!=0):
                if(Q==1):
                    ans=N//2+1
                else:
                    ans=N//2
            else:
                ans=N//2
        print(ans)
