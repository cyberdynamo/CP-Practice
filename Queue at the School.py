l,n=map(int,input().split())
string=input()
lst=list(string)
for j in range(n):
    i=0
    while(i<l-1):
        if(lst[i]=="B" and lst[i+1]=="G"):
            lst[i],lst[i+1]=lst[i+1],lst[i]
            i+=1
        i+=1
print("".join(lst))
