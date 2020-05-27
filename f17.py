import sys
def Luckey(string):
    for i in string:
        if(i!="4" and i!="7"):
            return False
    return True

num=int(input())
tempstr=str(num)
if(tempstr[0]=="-"):
    print("NO")
    sys.exit()
flag=0
for i in range(1,num+1):
    if(num%i==0):
        if(Luckey(str(i))==True):
            print("YES")
            flag=1
            break
if(flag==0):
    print("NO")
    
