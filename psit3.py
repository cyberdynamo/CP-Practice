test=int(input())
lst=[]
for t in range(test):
    op,string=input().split()
    count=0
    tmplst=list(string)
    if(op=="add"):
        lst.append(tmplst)
    else:
        for j in range(len(lst)):
            print(lst[j][:len(tmplst)],tmplst)
            if(lst[j][:len(tmplst)]==tmplst):
                count+=1
        print(count)
