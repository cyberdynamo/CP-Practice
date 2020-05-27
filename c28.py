import sys
n=1
while(n!=0):
    n=int(input())
    if(n==0):
        sys.exit()
    lst=list(map(int,input().split()))
    lst2=[0]*len(lst)

    for i in range(len(lst)):
        index=lst.index(lst[i])+1
        lst2[lst[i]-1]=index
    if(lst==lst2):
        print("ambigious")
    else:
        print("not ambigious")
    
