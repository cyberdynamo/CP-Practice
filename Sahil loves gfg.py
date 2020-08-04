test=int(input())
for t in range(test):
    string=input()
    if("gfg" not in string):
        print(-1)
    else:
        count=0
        for i in range(len(string)-2):
            print(i)
            tmp=string[i:i+3]
            if(tmp=="gfg"):
                count+=1
        print(count)
