for t in range(int(input())):
    n=int(input())
    x=0
    y=0
    for i in range(n):
        a,b=input().split()
        a=list(a)
        b=list(b)
        
        a=map(int,a)
        b=map(int,b)
        
        p=sum(a)
        q=sum(b)

        if(p>q):
            x+=1
        elif(p<q):
            y+=1
        else:
            x+=1
            y+=1

    if(x>y):
        print(0,x)
    elif(y>x):
        print(1,y)
    else:
        print(2,x)
