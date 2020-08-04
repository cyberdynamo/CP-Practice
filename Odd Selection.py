import itertools
test=int(input())
for t in range(test):
    a,b=map(int,input().split())
    lst=list(map(int,input().split()))
    flag2=0
    if(len(set(lst))==1):
        if((b*lst[0])%2!=0):
            print("Yes")
            flag2=1
        else:
            print("No")
            flag2=1
    if(flag2==0):
        s=0
        flag=0
        for i in itertools.combinations(lst,b):
            s=sum(i)
            if(s%2!=0):
                flag=1
                print("Yes")
                break
        if(flag==0):
            print("No")
