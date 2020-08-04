string=input()
even=[]
odd=[]
c=0
for i in string:
    if(i.isalnum()):
        c+=1
        if(i.isdigit()):
            if(int(i)%2==0):
                even.extend([int(i)])
            else:
                odd.extend([int(i)])
l=len(string)-c
print(l)
final=[]
if(l%2==0):
    if(len(even)>len(odd)):
        t=len(odd)
        out=even
    else:
        t=len(even)
        out=odd
    for i in range(t):
        final.extend([even[i],odd[i]])
    for j in out[t:]:
        final.extend([j])
else:
    if(len(odd)>len(even)):
        t=len(even)
        out=odd
    else:
        t=len(odd)
        out=even
    for i in range(t):
        final.extend([odd[i],even[i]])
    for j in out[t:]:
        final.extend([j])

final=list(map(str,final))
print("".join(final))
        
