string=input()
count=0
even=[]
odd=[]
for i in string:
    if(i.isalnum()!=True):
        count+=1
    if(i.isdigit()):
        if(int(i)%2==0):
            even.append(i)
        else:
            odd.append(i)

if(count%2==0):
    if(len(odd)>len(even)):
        tmplst=odd[len(even):]
        num=len(even)
    else:
        tmplst=even[len(odd):]
        num=len(odd)
    for i in range(num):
        print("{}{}".format(even[i],odd[i]),end="")
    tmplst=list(map(str,tmplst))
    print("".join(tmplst))
else:
    if(len(odd)>len(even)):
        tmplst=odd[len(even):]
        print(tmplst)
        print(even)
        print(odd)
        num=len(even)
    else:
        tmplst=even[len(odd):]
        num=len(odd)
    for i in range(num):
        print("{}{}".format(odd[i],even[i]),end="")
    tmplst=list(map(str,tmplst))
    print("".join(tmplst))
    
    
            
        
