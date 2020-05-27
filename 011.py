test=int(input())
t=1
for j in range(test):
    n,b=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    s=0
    i=0
    while(s<=b):
        s=s+l[i]
        i+=1
        
    print("Case #{}: {}".format(t,i-1))
    t+=1
