x=int(input())
t=x
if(360%x==0):
    print(360//x)
else:
    count=0
    while(x%360!=0):
        x+=t
        count+=1
    print(count+1)
