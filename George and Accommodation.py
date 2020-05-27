test=int(input())
count=0
for t in range(test):
    n,cap=map(int,input().split())
    if(cap-n>=2):
        count+=1
        
print(count)
