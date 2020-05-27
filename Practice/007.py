#EMP NAME and EMP NUMBER
lst=input().split(",")
name=[0]*len(lst)
number=[0]*len(lst)
for i in range(len(lst)):
    name[i], number[i]=lst[i].split(":")

def funct(name,number):
    l=len(name)
    while(l!=0):
        if(str(l) in number):
            return name[l-1]
        else:
            l-=1
    return "X"


for i in range(len(lst)):
    print(funct(name[i],number[i]),end="")
    
