def prime_seive(lst):
    for i in range(3,100005,2):
        lst[i]=1

    for i in range(3,100005,2):
        if(lst[i]==1):
            for j in range(i*i,100005,i):
                lst[j]=0
                
    lst[0]=0
    lst[1]=0
    lst[2]=1


lst=[0]*1000005
prime_seive(lst)
lst2=[0]*1000005
        
for i in range(1,1000005):
    lst2[i]=lst2[i-1]+lst[i]

test=int(input())
for t in range(test):
    a,b=map(int,input().split())
    print(lst2[b]-lst2[a-1])

        
