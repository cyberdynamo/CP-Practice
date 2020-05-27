lst=input()
c1,c2,c3,c4,c5=0,0,0,0,0
for i in range(len(lst)):
    if(lst[i]=="h"):
        c1=1
        break
if(i<len(lst)-1):
    for j in range(i,len(lst)):
        if(lst[j]=="e"):
            c2=1
            break
    if(j<len(lst)-1):
        for k in range(j,len(lst)):
            if(lst[k]=="l"):
                c3=1
                break
        if(k<len(lst)-1):
            for l in range(k+1,len(lst)):
                if(lst[l]=="l"):
                    c4=1
                    break
            if(l<len(lst)-1):
                for m in range(l,len(lst)):
                    if(lst[m]=="o"):
                        c5=1
                        break

if(c1==c2==c3==c4==c5==1):
    print("YES")
else:
    print("NO")
