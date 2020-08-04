#Fibonacci Numbers Recurssion

def Fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

if __name__=="__main__":
    print("Enter a number")
    m=int(input())
    print(Fib(m))
