# cook your dish here
def prime(number):
    flag=0
    for i in range(2,number//2+1):
        if(number%i==0):
            flag=1
    if(flag==0):
        return True
    else:
        return False
    
def factor(num,lst):
    sum1=0
    sum2=0
    for i in range(1,num//2+1):
        if(num%i==0):
            sum1+=1
        if(num%i==0 and prime(i)):
            sum2+=1
    lst.append(sum1+1)
    lst.append(sum2-1)
    return lst
test=input()
test=int(test)
for l in range(test):
    m,n=input().split()
    flag=0
    m=int(m)
    n=int(n)
    for i in range(1,1001):
        lst=[]
        factor(i,lst)
        tmp1=lst[0]
        tmp2=lst[1]
        if(tmp1==m and n==tmp2):
            print("1")
            flag=1
            break
    if(flag==0):
        print("0")
