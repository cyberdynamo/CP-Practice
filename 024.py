x=eval(input())
i=0
flag=0
l=[]
k=[]
while not flag:
    z=len(str(i))
    if(len(str(i))==x):
        l.append(i)
    if(z>x):
        flag=1
    i+=1
for i in l:
    if(str(i)==str(i)[::-1]):
        if(i%9==0):
            k.append(i)
flag1=0
ans=[]
for s in k:
    for j in str(s):
        if(j=='0'):
            k.remove(s)
sum=0
for i in k:
    sum+=i
print(sum%(10**9+7))
