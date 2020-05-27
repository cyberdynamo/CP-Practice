str1=input()
str2=input()
lst1=[]
lst2=[]
for i in str1:
    lst1.append(i.lower())
for i in str2:
    lst2.append(i.lower())
flag=0
for i in range(len(lst1)):
    if(lst1[i]<lst2[i]):
        print(-1)
        flag=1
        break
    elif(lst1[i]>lst2[i]):
        print(1)
        flag=1
        break
if(flag==0):
    print(0)
