test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    print(len(set(lst)))
