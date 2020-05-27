n,m,k,s=map(int,input().split())
flag=0
for i in range(n):
    lst=list(input().split()) 
    for j in range(m):
        if(j!=m-1):
            if(lst[j]=="."):
                s-=3
            elif(lst[j]=="*"):
                s+=4
            elif(lst[j]=="#"):
                break
        else:
            if(lst[j]=="."):
                s-=2
                break
            elif(lst[j]=="#"):
                break
            elif(lst[j]=="*"):
                s+=5
                break
    if(s<k):
        flag=1
        print("No")
        break
if(flag==0):
    print("Yes")
    print(s)
