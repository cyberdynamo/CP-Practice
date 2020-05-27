test=int(input())
for t in range(test):
    str1=input()
    str2=input()
    flag=0
    for i in range(len(str1)):
        if(str1[i]!="?" and str2[i]!="?" and str1[i]!=str2[i]):
            flag=1
        if(flag==1):
            break
    if(flag==1):
        print("No")
    else:
        print("Yes")        
