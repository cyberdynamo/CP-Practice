test=int(input())
for t in range(test):
    N=int(input())
    lst=list(map(int,input().split()))
    count=1
    for i in range(1,N):
        if(lst[i]>lst[i-1]):
            lst[i]=lst[i-1]
        else:
            count+=1
    print(count)
