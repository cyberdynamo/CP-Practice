test=int(input())
for t in range(test):
    s=input()
    lst=list(s)
    n=len(lst)
    s=list(set(lst))
    flag=1
    for i in s:
        tmp=lst.count(i)
        if(tmp==(n-tmp)):
            print("YES")
            flag=0
            break
    if(flag==1):
        print("NO")
