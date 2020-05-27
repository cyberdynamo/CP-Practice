test=int(input())
for _ in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    print(lst[0]+lst[1])
