openbr=["("]
closebr=[")"]
def checkBracket(string):
    stack=[]
    for i in range(len(string)):
        if(string[i] in openbr):
            stack.append(string[i])
        elif(string[i] in closebr):
            loc=closebr.index(string[i])
            if(len(stack)!=0 and openbr[loc]==stack[len(stack)-1]):
                stack.pop()
            else:
                return i+1
        if(len(stack)==0):
            return 0
        else:
            return(len(string)+1)

for t in range(int(input())):
    n=int(input())
    s=input()
    s=list(s)
    count=0
    while(checkBracket(s)!=0):
        count+=1
        z=checkBracket(s)
        z-=1
        print(z)
        s.pop(z)
    print(count)
        

    
