def fun1(a,b):
    s=0
    for i in b:
        s+=(int(i)**2)
    if(s%2==0):
        return a[-1:]+a[:-1]
    else:
        return a[2:]+a[:2]
        
lst=list(input().split(","))
for i in range(len(lst)):
    a,b=lst[i].split(":")
    print(fun1(a,b))
