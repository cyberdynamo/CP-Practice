test=int(input())
for t in range(test):
    n,m,d=map(int,input().split())
    temp=abs(n-m)
    if(temp<=d):
        print(0)
    else:
        print(temp-d)
