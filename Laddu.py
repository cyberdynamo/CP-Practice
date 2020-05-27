test=int(input())
for t in range(test):
    n,str1=input().split()
    n=int(n)
    count=0
    for i in range(n):
        string,*lst=input().split()
        if(len(lst)!=0):
            temp=lst[0]
            temp=int(temp)
            if(string=="CONTEST_WON"):
                if(temp<=20):
                    count+=300+20-temp
                else:
                    count+=300
            elif(string=="BUG_FOUND"):
                count+=temp
        else:
            if(string=="TOP_CONTRIBUTOR"):
                count+=300
            elif(string=="CONTEST_HOSTED"):
                count+=50
    if(str1=="INDIAN"):
        print(count//200)
    else:
        print(count//400)
