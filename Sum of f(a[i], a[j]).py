def Func(n,m):
    if(abs(n-m)>1):
        return m-n
    elif(abs(n-m)<=1):
        return 0

test=int(input())
for t in range(test):
    n=int(input())
    sum=0
    lst=list(map(int,input().split()))
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            sum+=Func(lst[i],lst[j])
    print(sum)
