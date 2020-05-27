test=int(input())
for t in range(test):
    string=input()
    lst=[]
    lst2=[]
    count=0
    count2=0
    for i in range(len(string)):
        if(string[i]=="A"):
            count+=1
            count2=0
            lst2.append(count)
        else:
            count2+=1
            count=0
            lst.append(count2)
    print(lst)
    print(lst2)
    maxi=max(lst)
    
