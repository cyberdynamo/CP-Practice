string=input()
c=0
even=[]
odd=[]
for i in string:
    if(i.isalnum()==True):
        c+=1
        if(i.isdigit()==True):
            if(int(i)%2==0):
                even.append(int(i))
            else:
                odd.append(int(i))
                
flist=[]
spcount=len(string)-c
if(spcount%2==0):
    if(len(even)>len(odd)):
        t=len(odd)
        out=even
        for i in range(t):
            flist.extend([even[i],odd[i]])
        for i in out[t:]:
            flist.append(i)
            
    else:
        t=len(even)
        out=odd
        for i in range(t):
            flist.extend([even[i],odd[i]])
        for i in out[t:]:
            flist.append(i)
else:
    if(len(odd)>len(even)):
        t=len(even)
        out=odd 
        for i in range(t):
            flist.extend([odd[i],even[i]])
        for i in out[t:]:
            flist.append(i)

    else:
        t=len(odd)
        out=even
        for i in range(t):
            flist.extend([odd[i],even[i]])
        for i in out[t:]:
            flist.append(i)

for i in flist:
    print(i,end="")
