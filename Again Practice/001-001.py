lst=list(map(int,input().split(",")))
n=len(lst)
num1=0
num2=0
i=0
while(i<n):
    if(lst[i]!=5):
        num1+=lst[i]
        i+=1
    elif(lst[i]==5):
        tmpstr=""
        while(lst[i]!=8):
            tmpstr+=str(lst[i])
            i+=1
        tmpstr+="8"
        i+=1
        num2+=int(tmpstr)
print(num1+num2)
