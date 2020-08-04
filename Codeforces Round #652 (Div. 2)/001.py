for t in range(int(input())):
    n=int(input())
    s=list(input())
    while(True):
        flag=0
        i=0
        while(i<n-1):
            if(s[i]=="1" and s[i+1]=="0"):
                flag=1
                tmplst=s[i+2:]
                if(len(tmplst)>=1):
                    if(s[i+2]=="0"):
                        del s[i+1]
                        n-=1
                    else:
                        del s[i]
                        n-=1
                elif(len(tmplst)==0):
                    del s[i+1]
                    n-=1
            i+=1
        if(flag==0):
            break
    print("".join(s))
