t=int(input()) 
for _ in range(1,t+1):
    n,k=map(int,input().split()) 
    li=list(map(int,input().split())) 
    count_list=[]
    num=0
    if k in li:
        count_k=li.count(k)
        for __ in range(count_k):
            index=li.index(k,num)
            num=index+1
            c=1
            for i in range(index,len(li)-1): 
                if li[i]-1 == li[i+1]:
                       c+=1        
                else:
                    break 
            if c == k: 
                count_list.append(c)
        length=len(count_list)  
        print("Case #{}: {}".format(_,length))         
    else:
        print("Case #{}: {}".format(_,0))
