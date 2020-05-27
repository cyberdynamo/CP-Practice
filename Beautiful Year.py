n=int(input())
while(True):
    n+=1
    m=n

    d1=m%10
    m=m//10
    d2=m%10
    m=m//10
    d3=m%10
    m=m//10
    d4=m%10
    if(len(set((d1,d2,d3,d4)))==4):
        break
print(n)
