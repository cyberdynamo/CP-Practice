test=int(input())
for t in range(test):
    lst=list(map(int,input().split()))
    s=set(lst)
    if(len(set(lst))==2):
        a=[]
        b=[]
        lst2=list(s)
        a.append(lst2[0])
        b.append(lst2[1])

        for i in lst:
            if(i in a):
                a.append(i)
            elif(i in b):
                b.append(i)
        if(len(a)==3 and len(b)==3):
            print("YES")
        else:
            print("NO")
    elif(len(s)==1):
        print("YES")
    else:
        print("NO")
        
