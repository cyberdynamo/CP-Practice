string=input()
count=0
flag=0
for i in range(len(string)-1):
    if(string[i]==string[i+1]):
        count+=1
    else:
        count=0
    if(count>=6):
        print("YES")
        flag=1
        break
if(flag==0):
    print("NO")
