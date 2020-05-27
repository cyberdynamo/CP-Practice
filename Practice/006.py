lst=input().split(",")
name=[0]*len(lst)
number=[0]*len(lst)
for i in range(len(lst)):
    name[i],number[i]=lst[i].split(":")

def funct(name, number):
    s=0
    while(number):
        d=number%10
        s+=(d**2)
        number//=10
        
    if(s%2==0):
        name=name[-1:]+name[:-1]
    else:
        name=name[2:]+name[:2]
    return name


for i in range(len(lst)):
    print(funct(name[i],int(number[i])),end=" ")
