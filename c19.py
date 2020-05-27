test=int(input())
for _ in range(test):
    lst=list(map(int,input().split()))
    print(max(lst),end=" ")
    print(sum(lst))
