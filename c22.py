test=int(input())
for _ in range(test):
    lst=list(map(int,input().split()))
    if(sum(lst)==180):
        print("YES")
    else:
        print("NO")
