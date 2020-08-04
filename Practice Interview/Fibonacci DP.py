#Fibonacci Numbers DP

def Fib(n):
    Fibo=[]
    Fibo.extend([0,1])
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        for i in range(2,n):
            Fibo.append(Fibo[i-1]+Fibo[i-2])
        print(Fibo)
        return Fibo[n-1]

print("Enter Number:")
m=int(input())
print(Fib(m))
