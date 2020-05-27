test=int(input())
for t in range(test):
    n,k=map(int,input().split())
    lst=input().split()
    flist=[]
    for i in range(k):
        n,*tmplst=input().split()
        flist.append(tmplst)

    for i in lst:
        flag=0
        for j in flist:
            if(i in j):
                flag=1
                print("YES",end=" ")
                break
        if(flag==0):
            print("NO",end=" ")
    print()
