test=int(input())
for t in range(test):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    count=0
    i=0
    while(i<n):
        flag2=0
        if(lst[i]==k):
            tmplst=lst[i:i+k]
            tmp=k
            flag=1
            if(len(tmplst)==k):
                for l in tmplst:
                    if(l!=tmp):
                        flag=0
                        break
                    tmp-=1
            if(flag==1 and len(tmplst)==k):
                count+=1
                i+=k
                flag2=1
        if(flag2==0):
            i+=1
            
    print("Case #{}: {}".format(t+1,count))
