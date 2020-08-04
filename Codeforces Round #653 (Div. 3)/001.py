for t in range(int(input())):
    x,y,n=map(int,input().split())

    q=n//x
    q-=1
    if(q*x+y<0):
        print(0)
    else:
        print(q*x+y)
