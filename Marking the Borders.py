for t in range(int(input())):
    a,b,L,R=map(int,input().split())
    count=0
    c=0
    while(True):
        c+=a
        print(c)
        a,b=b,a

        if(c>=L and c<=R):
            count+=1
        if(c>R):
            break
    print(count)
