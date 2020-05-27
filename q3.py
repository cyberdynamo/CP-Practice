test=int(input())
for i in range(test):
    str1=input()
    count1=0
    for j in str1:
        if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u" ):
            count1+=1
    print(count1,(len(str1)-count1),(count1*(len(str1)-count1)))
        
