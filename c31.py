test=int(input())
for _ in range(test):
    string=input()
    l=len(string)
    str1=string[:l//2]
    str2=string[l-(l//2):]

    dict1={}
    dict2={}

    for i in range(len(str1)):
        temp=str1[i]
        flag=0

        for j in dict1.keys():
            if(j==temp):
                flag=1

        if(flag==0):
            dict1.update({temp:1})
        else:
            for j in dict1.items():
                if(j[0]==temp):
                    q=j[1]
                    q+=1
                    dict1.update({temp:q})



    for i in range(len(str2)):
        temp=str2[i]
        flag=0

        for j in dict2.keys():
            if(j==temp):
                flag=1

        if(flag==0):
            dict2.update({temp:1})
        else:
            for j in dict2.items():
                if(j[0]==temp):
                    q=j[1]
                    q+=1
                    dict2.update({temp:q})


    if(dict1==dict2):
        print("YES")
    else:
        print("NO")


    
