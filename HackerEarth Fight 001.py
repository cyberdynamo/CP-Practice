n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
m=int(input())
for j in range(m):
    a,b,s=input().split()
    a=int(a)
    b=int(b)
    count=0
    for k in range(a-1,b):
        if(s==lst[k]):
            count+=1
    print(count)
