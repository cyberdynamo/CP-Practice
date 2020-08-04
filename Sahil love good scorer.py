test=int(input())
for t in range(test):
    a,b=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    if(sum(lst1)>sum(lst2)):
        print("C1")
    else:
        print("C2")
