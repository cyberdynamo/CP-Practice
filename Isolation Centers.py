import sys
test=int(input())
for t in range(test):
    n,q=map(int,input().split())
    string=input()
    dict1={}
    for i in range(n):
        if(string[i] not in dict1):
            dict1.update({string[i]:1})
        else:
            temp=dict1.get(string[i])
            dict1.update({string[i]:temp+1})
    lst2=list(dict1.values())
    flist=lst2.copy()
    for j in range(q):
        temp=int(input())
        lst2=flist.copy()
        for m in range(len(lst2)):
            if(lst2[m]-temp<=0):
                lst2[m]=0
            else:
                lst2[m]-=temp
        print(sum(lst2))
