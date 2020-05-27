n=int(input())
count=0
while(n):
    d=n%10
    count+=1
    n=n//10
    if(count>3):
        break
if(count==1):
    print(1)
elif(count==2):
    print(2)
elif(count==3):
    print(3)
else:
    print("More than 3 digits")
