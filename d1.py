test=int(input())
for k in range(test):
    l,a,b=map(int,input().split())
    lst=[]
    lst.append(a)
    lst.append(b)
    lst.append((a+b)%10)
    for i in range(3,l):
        lst.append((lst[i-1]*2)%10)
    str1=""
    for j in lst:
        str1+=str(j)
    print(str1)
    

