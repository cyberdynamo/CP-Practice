test=int(input())
for t in range(test):
    n,k=map(int,input().split())

    lst=list(map(int,input().split()))
    tmplst=lst[-k:]+lst[:-k]
    print(*tmplst)
