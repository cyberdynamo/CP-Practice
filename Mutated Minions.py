for t in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    count=0
    for i in lst:
        if((i+k)%7==0):
            count+=1
    print(count)
