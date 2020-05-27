test=int(input())
for _ in range(test):
    n=int(input())
    lst=[]
    lst.append(n)
    while(lst[-1]!=1):
        if(lst[-1]%2==0):
            lst.append(lst[-1]//2)
        else:
            lst.append(3*lst[-1]+1)
    print(len(lst)-1)
    
