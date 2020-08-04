s=input()
count1=0
count2=0
for i in range(len(s)):
    if(i%2==0):
        if(s[i]!="S"):
            count1+=1
    elif(i%2!=0):
        if(s[i]!="R"):
            count1+=1


for i in range(len(s)):
    if(i%2==0):
        if(s[i]!="R"):
            count2+=1
    elif(i%2!=0):
        if(s[i]!="S"):
            count2+=1
print(min(count1,count2))
