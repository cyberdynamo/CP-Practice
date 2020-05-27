test=int(input())
for t in range(test):
    n=int(input())
    lst=[0]*n
    for i in range(n):
        lst[i]=int(input())
    print(lst)
    s=0
    for i in range(n):
        if(lst[i]%2!=0):
            s+=1
    print(s)
