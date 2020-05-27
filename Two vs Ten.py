test=int(input())
for t in range(test):
    n=int(input())

    temp=n%10
    if(temp==0):
        print(0)
    elif(temp==5):
        print(1)
    else:
        print(-1)
