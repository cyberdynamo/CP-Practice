s=input()
count=0
count2=0
if(("c" in s)or("k" in s)):
    print(0)
else:
    for i in range(len(s)-1):
        if((s[i]==s[i+1]=="f")or(s[i]==s[i+1]=="g")):
            count+=1
        if(i!=0 and i!=(len(s)-1)):
            if((s[i]==s[i+1]==s[i-1]=="f") or (s[i]==s[i-1]==s[i+1]=="g")):
                count2+=1
    if(count2==0):
        print(2**count)
    else:
        print(2**(count2)+1)
