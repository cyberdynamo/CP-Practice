def CheckBr(string):
    stack=[]
    for i in range(len(string)):
        if(string[i] in openbr):
            stack.append(string[i])
        elif(string[i] in closebr):
            loc=closebr.index(string[i])
            if(len(stack)!=0 and openbr[loc]==stack[-1]):
                stack.pop()
            else:
                return i+1
    if(len(stack)==0):
        return 0
    else:
        return len(string)+1

string=input()
openbr=["(","[","{"]
closebr=[")","]","}"]
print(CheckBr(string))
