n=int(input())
d={}
c=(n*5)/100
for i in range(n):
    m=input()
    if(m not in d):
        d.update({m:1})
    else:
        t=d[m]
        d[m]=t+1
final=[]
for i in d.items():
    if(i[1]>=c):
        final.append(i[0])
final.sort()
for j in final:
    print(j)
