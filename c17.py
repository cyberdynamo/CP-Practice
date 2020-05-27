test=int(input())
for _ in range(test):
    tmp=0
    num=int(input())
    lst=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    for i in range(len(lst)):
        if(lst[i]>num):
            break
    if(num>=2048):
        tmp=num//2048
        num=num-(tmp*2048)
    newlst=lst[:i]
    newlst=newlst[::-1]
    s=0
    count=0
    while(s!=num):
        for i in range(len(newlst)):
            if(s+newlst[i]<=num):
                s+=newlst[i]
                count+=1
    print(count+tmp)
