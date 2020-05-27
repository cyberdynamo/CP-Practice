test=int(input())
for t in range(test):
    n,d=map(int,input().split())
    lst=list(map(int,input().split()))
    newlst=lst[d:]+lst[:d]
    for i in range(len(newlst)-1):
        print(newlst[i],end=" ")
    print(newlst[-1])
