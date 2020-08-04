for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))

    d={}
    for i in range(len(lst)):
        if(lst[i] not in d):
            d.update({lst[i]:1})
        else:
            d[lst[i]]+=1
    l=[]
    for i in d.items():
        l.append([i[1],i[0]])
    l.sort(reverse=True)
    area=1
    count=0
    flag=0
    for i in range(len(l)):
        if(l[i][0]>=4):
            flag=1
            area=l[i][1]*l[i][1]
            break
        if(count==2):
            break
        if(l[i][0]>=2):
            area*=l[i][1]
            count+=1
    if(count==2 or flag==1):
        print(area)
    else:
        print(-1)
