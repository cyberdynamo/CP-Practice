import math
def numberhaveodddiv(n,lst):
    for i in range(3,n//2+1):
        if(n%i==0 and i%2!=0):
            lst.append(i)
            return True
    return False

for t in range(int(input())):
    n=int(input())
    if(n==1):
        print("FastestFinger")
    if(n==2):
        print("Ashishgup")
    elif(n%2!=0):
        print("Ashishgup")
    else:
        c=0
        lst=[]
        while(numberhaveodddiv(n,lst)):
            c+=1
            n=n//lst[0]
        if(c%2==0):
            print("FastestFinger")
        else:
            print("Ashishgup")
        
