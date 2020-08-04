test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    i=0
    s=0
    while(i!=n):
        p=lst[i]
        if(p-1 in lst):
            lst.remove(p-1)
            n-=1
        s+=lst[i]
        i+=1
    print(s)
        
        
