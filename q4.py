test=int(input())
for i in range(test):
    str1=input()

    c1,c2,c3,c4=0,0,0,0
    for i in str1:
        if(i.isalnum()):
            if(i.isalpha()):
                if(i.isupper()):
                    c1+=1
                elif(i.islower()):
                    c2+=1
            else:
                c3+=1
        else:
            c4+=1
    if(c1==c2==c3==c4):
        print("Equality For Everyone")
    else:
        print("No Equality")
        
            
