test=int(input())
for _ in range(test):
    m,r1,r2,r3=map(int,input().split())
    num=m%4
    if(num==0):
        print(0)
    elif(num==3):
        print(r1)
    elif(num==2):
        lst=[]
        lst.append(2*r1)
        lst.append(r2)
        print(min(lst))
    else:
        lst=[]
        lst.append(r3)
        lst.append(3*r1)
        lst.append(r2+r1)
        print(min(lst))
        
