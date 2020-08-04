import math
n=int(input())
x=str(n)
l=[]
for i in range(len(x)):
    for j in range(i,len(x)):
        l.append(int(x[i:j+1]))
w=[]
for i in l:
    if i not in w:
        w.append(i)
#w.sort()
for i in w:
    j=0
    while j<=int(math.sqrt(i)):
        if(i==j*(j+1)):
            print(i,end=" ")
            break
        j+=1
