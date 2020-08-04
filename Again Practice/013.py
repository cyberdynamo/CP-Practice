#HelLoWOrld Output:dWerHoOlLl
k=input()
ss=sorted(set(k.upper()))
fin=[]
for i in range(len(ss)):
    s=""
    for j in k:
        if ss[i]==j.upper():
            s+=j
    fin.append(s)

i=0
j=len(fin)-1
out=""
while i<=j:
    if i==j:
        out+=fin[i]
    else:
        out+=fin[i]+fin[j]
    i+=1
    j-=1
print(out)
