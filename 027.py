testcases=int(input())
def NotContain(number):
    while(number!=0):
        d=number%10
        if(d==4):
            return False
        else:
            number=number//10
    return True
      
for i in range(1,testcases+1):
    n=int(input())
    for j in range(1,n):
        temp=n-j
        if(NotContain(j) and NotContain(temp)):
            print("Case #"+str(i)+": "+ str(j) + " "+str(temp))
            break
