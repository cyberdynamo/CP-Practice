n=int(input())
s=input()
i,j=0,0
c=0
str1=""
while(i!=(n-1)):
    temp=s[i:i+2]
    count=0
    j=0
    while(j!=(n-1)):
        if(s[j:j+2]==temp):
            count+=1
        j+=1
    if(count>c):
        c=count
        str1=temp
    i+=1
print(str1)
