test=int(input())
for t in range(test):
    n=int(input())
    lst1=list(map(int,input().split()))
    m=int(input())
    lst2=list(map(int,input().split()))
    f=0
    for i in range(n-m):
        if(lst1[i:i+m]==lst2):
            print("Yes")
            f=1
            break
    if(f==0):
        print("No")
        
