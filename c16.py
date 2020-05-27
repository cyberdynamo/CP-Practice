test=int(input())
for k in range(test):
    x=0
    num=int(input())
    lst=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    for i in range(len(lst)):
        if(lst[i]>num):
            break
    lst2=lst[:i]
    lst2=lst2[::-1]
    if(num>=2048):
        x=num//2048
        num=num%(x*2048)
        lst2=lst[::-1]
    s=0
    count=0
    while(s!=num):
        for j in range(len(lst2)):
            if((s+lst2[j])<=num):
                s+=lst2[j]
                count+=1
    print(count+x)
    x=0

