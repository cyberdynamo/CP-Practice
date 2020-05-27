test=int(input())
for t in range(test):
    a,b=map(int,input().split())
    x=0;y=0
    p=1;q=2
    f=0
    while(True):
        x+=p
        p+=2
        y+=q
        q+=2

        if(x>a):
            f=1
            break
        if(y>b):
            f=2
            break
    if(f==1):
        print("Bob")
    else:
        print("Limak")
