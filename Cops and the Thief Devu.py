test=int(input())
for t in range(test):
    Q,m,n=map(int,input().split())
    lst=list(map(int,input().split()))
    lst2=[1]*100
    c=m*n
    for i in range(len(lst)):
        temp=lst[i]-1
        start,end=0,0
        if(temp-c<=0):
            start=0
        else:
            start=temp-c

        if(temp+c>=99):
            end=99
        else:
            end=temp+c

        for j in range(start,end+1):
            lst2[j]=0
            
        for k in range(start,end+1):
            lst2[k]=0
    count=0
    for l in range(len(lst2)):
        if(lst2[l]==1):
            count+=1
    print(count)
