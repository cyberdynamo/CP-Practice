test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    k=int(input())
    lst.sort()
    print(lst[k-1])
