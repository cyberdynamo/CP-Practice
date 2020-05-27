test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    count=0
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if(lst[i]^lst[j]==0):
                count+=1
    print(count)
