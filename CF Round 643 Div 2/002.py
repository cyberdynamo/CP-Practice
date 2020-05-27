test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    count=0
    i=0
    while(i<n):
        temp=lst[i]
        count+=1
        i+=temp
    print(count)
