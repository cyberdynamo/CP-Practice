test=int(input())
for t in range(test):
    n=int(input())
    lst=list(map(int,input().split()))
    if(len(lst)%2==0):
        lst1=lst[:n//2]
        lst2=lst[n//2:]
        lst2.reverse()
        s1=set(lst1);s2=set(lst2)
        f=0
        for i in range(len(lst1)-1):
            if(lst1[i+1]<lst1[i] or s1!={1,2,3,4,5,6,7}):
                print("no")
                f=1
                break
            elif(lst2[i+1]<lst2[i] or s2!={1,2,3,4,5,6,7}):
                print("no")
                f=1
                break
        if(f==0):
            if(lst1==lst2):
                print("yes")
            else:
                print("no")
                
    else:
        lst1=lst[:(n-1)//2]
        lst2=lst[(n-1)//2+1:]
        lst2.reverse()
        f=0
        if(lst.count(7)==1):
            s1=set(lst1);s2=set(lst2)
            for i in range(len(lst1)-1):
                if(lst1[i+1]<lst1[i] or s1!={1,2,3,4,5,6}):
                    print("no")
                    f=1
                    break
                elif(lst2[i+1]<lst2[i] or s2!={1,2,3,4,5,6}):
                    print("no")
                    f=1
                    break
        else:
            s1=set(lst1);s2=set(lst2)
            for i in range(len(lst1)-1):
                if(lst1[i+1]<lst1[i] or s1!={1,2,3,4,5,6,7}):
                    print("no")
                    f=1
                    break
                elif(lst2[i+1]<lst2[i] or s2!={1,2,3,4,5,6,7}):
                    print("no")
                    f=1
                    break
            
        if(f==0):
            if(lst1==lst2 and lst[n//2]==7):
                print("yes")
            else:
                print("no")
