test=int(input())
for t in range(test):
    n,k=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))

    lst1.sort()
    lst2.sort(reverse=True)
    flag=0
    for i in range(n):
        if(lst1[i]+lst2[i]<k):
            flag=1
    if(flag==0):
        print("YES")
    else:
        print("NO")
