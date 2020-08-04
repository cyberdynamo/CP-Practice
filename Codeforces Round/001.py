for t in range(int(input())):
    n,x=map(int,input().split())
    lst=list(map(int,input().split()))
 
    lst2=[]
    lst2.append(lst[0])
    for i in range(1,len(lst)):
        lst2.append(lst2[i-1]+lst[i])
    maxi=0
    f=0
    for i in range(len(lst2)):
        for j in range(i+1,len(lst2)):
            if(lst[i]%x!=0):
                f=1
            if((lst2[j]-lst2[i]+lst[i])%x!=0 and (j-i+1)>maxi):
                maxi=j-i+1
    if(maxi==0 and f==1):
        print(1)
    elif(maxi==0):
        print(-1)
    else:
        print(maxi)
