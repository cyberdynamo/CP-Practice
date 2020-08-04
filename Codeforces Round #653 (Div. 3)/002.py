for t in range(int(input())):
    x,y,n=map(int,input().split())

    q=n//x
    s=q*x
    if(s+y>n):
        q-=1
        s=q*x
        print(s+y)
    else:
        print(s+y)
