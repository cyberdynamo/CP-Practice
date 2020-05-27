test=int(input())
for i in range(test):
    temp=int(input())
    count=0
    while(temp!=0):
        d=temp%10
        if(d==4):
            count+=1
        temp=temp//10
    print(count)
        
