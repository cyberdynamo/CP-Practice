for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    even=[]
    odd=[]
    for i in range(len(lst)):
        if(lst[i]%2==0):
            even.append([lst[i],i])
        else:
            odd.append([lst[i],i])

    l1=len(even)
    l2=len(odd)

    flag=0
    if(l1%2==0 and l2%2==0):
        flag=1
    elif((l1-1)%2==0 and (l2-1)%2==0):
        flag=2

    if(flag==1):
        if(len(odd)>=2):
            odd.remove(min(odd))
            odd.remove(min(odd))
        else:
            even.remove(min(even))
            even.remove(min(even))
        c=0
        for i in range(len(even)):
            print(even[i][1]+1,end=" ")
            c+=1
            if(c%2==0):
                print()
        for i in range(len(odd)):
            print(odd[i][1]+1,end=" ")
            c+=1
            if(c%2==0):
                print()
    
    elif(flag==2):
        a=min(odd)
        b=min(even)
        odd.remove(a)
        even.remove(b)
        c=0
        for i in range(len(even)):
            print(even[i][1]+1,end=" ")
            c+=1
            if(c%2==0):
                print()
        for i in range(len(odd)):
            print(odd[i][1]+1,end=" ")
            c+=1
            if(c%2==0):
                print()
        
