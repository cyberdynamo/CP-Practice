for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))

    s=0
    for i in range(1,len(lst)):
        s+=(abs(lst[i]-lst[i-1])-1)
    print(s)
