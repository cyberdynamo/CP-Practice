test=int(input())
for t in range(test):
    string=input()
    l=len(string)
    str1=string[:l//2]
    str2=string[l-l//2:]
    dict1={}
    dict2={}
    for i in range(len(str1)):
        if(str1[i] not in dict1.keys()):
            dict1.update({str1[i]:1})
        else:
            temp=dict1.get(str1[i])
            dict1.update({str1[i]:temp+1})
    
    for j in range(len(str2)):
        if(str2[j] not in dict2.keys()):
            dict2.update({str2[j]:1})
        else:
            temp=dict2.get(str2[j])
            dict2.update({str2[j]:temp+1})

    if(dict1==dict2):
        print("YES")
    else:
        print("NO")
    
            
        
    
