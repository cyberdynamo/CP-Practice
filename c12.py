n=int(input())
pl1=[]
pl2=[]
for i in range(n):
    n,m=map(int,input().split())
    pl1.append(n)
    pl2.append(m)

new1=[]
new2=[]
for i in range(len(pl1)):
    temp1=sum(pl1[:i+1])
    temp2=sum(pl2[:i+1])
    new1.append(temp1)
    new2.append(temp2)

flst=[]
ab=0
maxi=0
for i in range(len(new1)):
    temp=abs(new1[i]-new2[i])
    if(temp>maxi):
        maxi=temp

        if(new1[i]>new2[i]):
            ab=1
        else:
            ab=2
print(ab,maxi)
        
    




    
