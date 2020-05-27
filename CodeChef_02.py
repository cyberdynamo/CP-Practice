test=int(input())
for i in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    num=0
    s=0
    lst.sort(reverse=True)
    for j in lst:
        if(j-num>0):
            s=s+(j-num)
        else:
            pass
        num+=1
    print(s%((10**9)+7))
        
        
