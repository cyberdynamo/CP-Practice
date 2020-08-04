for test in range(int(input())):
    a,b=map(int,input().split())
    if(a<b):
        if(b%2!=0 or b%a!=0):
            print(-1)
        else:
            temp=b//a
            count=0
            while(temp==4 or temp==2):
                count+=1
                temp//=8
            if(temp!=0 and temp%4==0):
                count+=1
                temp//=4
            if(temp!=0 and temp%2==0):
                count+=1
                temp//=2
            print(count)
