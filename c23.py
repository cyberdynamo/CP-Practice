test=int(input())
for _ in range(test):
    tmp=0
    num=int(input())
    lst=[1,2,5,10,50,100]
    for i in range(len(lst)):
        if(lst[i]>num):
            break
    if(num>=100):
        tmp=num//100
        num=num-(tmp*100)
    newlst=lst[:i]
    newlst=newlst[::-1]
    s=0
    count=0
    while(s!=num):
        for i in range(len(newlst)):
            if(s+newlst[i]<=num):
                s+=newlst[i]
                count+=1
                break
    print(count+tmp)
