n=int(input())
lst=list(map(int,input().split()))
a=lst.count(1)
b=lst.count(2)
c=lst.count(3)
d=lst.count(4)
count=d
if(a!=0 and c!=0):
    if(a<c):
        count+=min(a,c)
        c=c-a
        a=0
        count+=((b%2==0?b//2:b//2+1))
        count+=c
    elif(a>c):
        count+=min(a,c)
        a=a-c
        c=0
        
else:
    if(a==0 and c==0):
        count+=((b%2==0?b//2:b//2+1))
    if(a==0):
        count+=c
        count+=((b%2==0?b//2:b//2+1))
    elif(c==0):
        if(b*2>=a):
            a=a-1
            count+=a//2
            temp=b-a//2
            count+=((temp%2==0?temp//2:temp//2+1))
            
                
            
            
        
print(count)


    
