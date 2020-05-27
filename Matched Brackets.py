n=int(input())
lst=list(map(int,input().split()))
count,maxi,count2,maxi2=0,0,0,0
for i in range(len(lst)):
    if(lst[i]==1):
        count+=1
    else:
        count-=1
    if(count>maxi):
        maxi=count
        temp=i+1
        
    if(count!=0):
        count2+=1
        if(count2>maxi2):
            maxi2=count2
            temp2=i+1
    else:
        count2=0
print(maxi,temp,maxi2+1,temp2-maxi2+1)
