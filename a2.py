test=int(input())
lst=[]
for _ in range(test):
    for k in range(9):
        tmplst=input()
        for i in range(len(tmplst)-1):
            if(tmplst[i]=="2"):
                print("1",end="")
            else:
                print(tmplst[i],end="")
        if(tmplst[-1]=="2"):
            print("1")
        else:
            print(tmplst[-1])
