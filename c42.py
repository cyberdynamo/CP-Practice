n,k=map(int,input().split())
lst=[]
for i in range(k):
    clk,*num=input().split()
    if(len(num)==0):
        lst=[]
        print(0)
    else:
        num=num[0]
        if(num not in lst):
            lst.append(num)
            print(len(lst))
        else:
            lst.remove(num)
            print(len(lst))
    
    
