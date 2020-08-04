for t in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    if(1 not in lst):
        print(0)
    else:
        a=lst.index(1)
        for i in range(n-1,-1,-1):
            if(lst[i]==1):
                break
        b=i
        if(a==b):
            print(0)
        else:
            #list1=lst[:a]
            #list2=lst[b+1:]
            #l1=len(list1)
            #l2=len(list2)

            i#f((l1+l2+1)<(b-a)):
                #print(l1+l2+1)
            #else:
            print((b-a))
            
        
        
        
    
