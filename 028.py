test=int(input())
for i in range(1,test+1):
    temp=int(input())
    lst=[]
    for j in range(temp):
        lst.append(list(map(int,input().split())))
    sum=0
    for p in range(temp):
        for q in range(temp):
            if(p==q):
                sum+=lst[p][q]
    rowsum=0
    for a in range(len(lst)):
        tempset=set(lst[a])
        if(len(tempset)!=len(lst[a])):
            rowsum+=1
            
    colsum=0
    for l in range(len(lst[0])):
        newlist=[]
        for k in range(temp):
            newlist.append(lst[k][l])
        new2set=set(newlist)
        if(len(newlist)!=len(new2set)):
            colsum+=1
                   
    print("Case# {}: {} {} {}".format(i,sum,rowsum,colsum))
