test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    list1=[]
    list1.append(lst[0])
    list2=[]
    list2.append(lst[0])
    for i in range(1,n):
        list1.append(lst[i]+list1[i-1])
        list2.append(lst[i]*list2[i-1])
    print(list1,list2)
    count=0

    for i in range(n-1):
        for j in range(i+1,n):
            if(list1[j]-list1[i]+list1[i]==(list2[j]//list2[i])*list2[i]):
                count+=1
    print(count)
