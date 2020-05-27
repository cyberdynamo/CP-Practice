import math
def distance(a,b,c,d):
    return int(math.sqrt((a-c)**2+(b-d)**2))

test=int(input())
for _ in range(test):
    num=int(input())
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    e,f=map(int,input().split())

    d1=distance(a,b,c,d)
    d2=distance(c,d,e,f)
    print(d1,d2)
    if(num>=d1 and num>=d2):
        print("yes")
    else:
        print("no")
    
