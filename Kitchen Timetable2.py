test=int(input())
for t in range(test):
    n=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    s=0
    if(lst2[0]<=lst1[0]):
        s+=1
    for i in range(1,n):
        if((lst1[i]-lst1[i-1])>=(lst2[i])):
            s+=1
    print(s)
