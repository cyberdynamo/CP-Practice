test=int(input())
for t in range(test):
    n,m,k=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    count1=0
    count2=0
    for i in lst1:
        if(i in lst2):
            count1+=1

    set1=set(lst1)
    set2=set(lst2)
    fset=set1.union(set2)
    count2=n-len(fset)
    print(count1,count2)
