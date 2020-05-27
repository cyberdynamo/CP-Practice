test=int(input())
for _ in range(test):
    str1=input()
    str2=input()

    #Minimum
    count=0
    for i in range(len(str1)):
        if(str1[i]!="?" and str2[i]!="?"):
            if(str1[i]!=str2[i]):
                count+=1

    #Maximum
    c1=0
    for i in range(len(str1)):
        if(str1[i]=="?" and str2[i]=="?"):
            c1+=1
        elif(str1[i]=="?" and str2[i]!="?"):
            c1+=1
        elif(str1[i]!="?" and str2[i]=="?"):
            c1+=1
            
    count2=count+c1
    print(count,count2)
                
            
