def CheckNo(number):
    temp=number
    s=0
    while(number!=0):
        d=number%10
        s=s+d
        number=number//10
    if(temp%s==0):
        return True
    else:
        return False

row=int(input())
lst=[]
for i in range(row):
    lst.append(list(map(int,input().split())))
col=len(lst[0])
flag=0
for i in range(row-1):
    for j in range(col-1):
        if(CheckNo(lst[i][j]) and CheckNo(lst[i][j+1]) and CheckNo(lst[i+1][j]) and CheckNo(lst[i+1][j+1])):
            print(lst[i][j],lst[i][j+1])
            print(lst[i+1][j],lst[i+1][j+1],end="\n")
            flag=1
if(flag==0):
    print("-1")


            
    
        
    
