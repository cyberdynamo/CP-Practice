num=int(input())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
s,count=0,0
i=0
while(True):
    s+=lst[i]
    if(s>sum(lst)/2):
        break
    count+=1
    i+=1
print(count+1)
    
    
