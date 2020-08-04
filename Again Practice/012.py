a=int(input())
b=str(a)
n=len(b)
c=[]
k=0
l=0
for i in range(n):
    k=0
    l=i
    if(i==0):
        for j in range(n):
            c.append(int(b[j]))
    else:
        for j in range(n-i):
            c.append(int(b[k:l+1]))
            k=k+1
            l=l+1
d=[]
for i in c:
    if(i not in d):
        d.append(i)
d=sorted(d)
for i in d:
    for j in range(1,150):
        if(j*(j+1)==i):
            print(i,end=',')
