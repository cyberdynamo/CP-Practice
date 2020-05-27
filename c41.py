test=int(input())
for t in range(test):
    lst=[]
    n,k=map(int,input().split())
    for i in range(1,k+1):
        lst.append(n%i)
    print(max(lst))
