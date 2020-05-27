test=int(input())
for i in range(test):
    str1=input()
    num=input()

    lst=[]
    for j in range(len(num)):
        str2=""
        for k in range(j+1):
            str2+=num[k]
        lst.append(str2)
        
    flist=[]
    for j in range(len(lst)):
        q=int(lst[j])
        q=q%26
        flist.append(q)
    print(flist)
    fstr=""
    for j in range(len(str1)):
        n=ord(str1[j][0])
        print(n)
        if(n+flist[j]<=122):
            n=n+flist[j]
            n=chr(n)
            fstr+=n
        print(fstr)

        
            
