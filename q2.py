test=int(input())
for k in range(test):
    num=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    lst2.sort()
    count=0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if(lst1[i]>lst2[j]):
                count+=1
                lst2[j]=999999
                break
        print(lst1)
        print(lst2)
    print(count)
            
