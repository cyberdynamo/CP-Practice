test=int(input())
for t in range(test):
    n=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))

    flst=[]
    for i in range(n):
        flst.append([lst1[i]*lst2[i],lst2[i],199-i])
    flst.sort(reverse=True)
    print(199-flst[0][2]+1)
