for t in range(int(input())):
    n=int(input())
    c1,c2,c3=0,0,0
    s=input()
    for i in s:
        if(i=="R"):
            c1+=1
        elif(i=="G"):
            c2+=1
        else:
            c3+=1

    lst=[c1,c2,c3]
    lst.sort()
    print(lst[0]+lst[1])
