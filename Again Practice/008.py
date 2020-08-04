def fun1(a,b):
    l=len(a)
    while(l!=0):
        if(str(l) in b):
            return a[l-1]
        else:
            l-=1
    if(l==0):
        return "" 
    else:
        return "X"


lst=list(input().split(","))
str1=""
for i in range(len(lst)):
    a,b=lst[i].split(":")
    str1+=fun1(a,b)
print(str1)
