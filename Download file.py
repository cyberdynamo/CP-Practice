test=int(input())
for t in range(test):
    n,k=map(int,input().split())
    counter=0
    ans=0
    flag=0
    var1,var2,var3=0,0,0
    i=0
    for i in range(n):
        a,b=map(int,input().split())
        counter+=a
        if(counter>k):
            var1,var2=a,b
            var3=counter-k
            break
    ans+=(var3*var2)
    for j in range(i+1,n):
        x,y=map(int,input().split())
        ans+=(x*y)
    print(ans)
