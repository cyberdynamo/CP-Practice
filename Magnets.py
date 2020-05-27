n=int(input())
temp=int(input())
d1=temp%10
temp=temp//10
d2=temp%10
count=1
for i in range(n-1):
    temp=int(input())
    d3=temp%10
    temp=temp//10
    d4=temp%10

    if(d1==d4):
        count+=1
    d1=d3
    d2=d4
print(count)
