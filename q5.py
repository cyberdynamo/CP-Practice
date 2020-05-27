str1=input()
num=input()

lst=[]

for i in range(len(num)):
    str2=""
    for j in range(i+1):
        str2+=num[j]
    lst.append(str2)
flist=[]
for i in lst:
    i=int(i)
    i=i%26
    flist.append(i)
glist=[]
for k in str1:
    k+=1
    glist.append(k)
print(glist)
    
