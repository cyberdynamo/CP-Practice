n=int(input())
count=0
for _ in range(n):
    a,b,c=map(int,input().split())
    c2=0
    if(a==1):
        c2+=1
    if(b==1):
        c2+=1
    if(c==1):
        c2+=1
    if(c2>=2):
        count+=1
print(count)
