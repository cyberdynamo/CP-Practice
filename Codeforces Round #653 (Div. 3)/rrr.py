for t in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))

    x=0
    count=0
    while(True):
        flag=0
        for i in range(len(lst)):
            if(lst[i]!=0 and lst[i]%k!=0):
                flag=1
                if((lst[i]+x)%k==0):
                    lst[i]=lst[i]+x
                    count+=1
                    x+=1
                    break
            if(i==n-1 and (lst[i]!=0 and lst[i]%k!=0)):
                x+=1
                count+=1
                break
        if(flag==0):
            break
    print(count)
