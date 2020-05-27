import math
test=int(input())
def possible(num,lst):
    a=-1+(math.sqrt(1+8*num))
    b=-1-(math.sqrt(1+8*num))
    if(a%2==0 and a>0):
        lst[0]=a//2
        return True
    elif(b%2==0 and b>0):
        lst[0]=b//2
        return True
    else:
        return False
    
for t in range(test):
    n=int(input())
    lst=[0]
    while(n!=0):
        if(possible(n,lst)==True):
            print(int(lst[0]))
            break
        n-=1
