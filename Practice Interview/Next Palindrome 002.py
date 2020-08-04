import math
def helper(number):
    newnumber=""
    if(len(number)%2==0):
        for i in range(len(number)//2):
            newnumber+=str(number[i])
        newnumber+=newnumber[::-1]
        return int(newnumber)
    else:
        for i in range(len(number)//2+1):
            newnumber+=str(number[i])
        newnumber+=newnumber[:len(number)//2][::-1]
        return int(newnumber)

def solve(number):
    number2=helper(number)
    number=list(map(str,number))
    number="".join(number)
    number=int(number)
    if(number2>number):
        return number2
    else:
        #Increase the Middle Char
        for i in range(math.ceil(len(number2)))
        
        

N=int(input())
for i in range(N):
    number=list(input())
    number=list(map(int,number))

    if(len(set(number))==1 and number[0]==9):
        tmpstr=""
        for j in range(len(number)):
            tmpstr+=str(number[j])
        tmpstr=int(tmpstr)
        tmpstr+=2
        print(tmpstr)
    else:
        print(solve(number))
