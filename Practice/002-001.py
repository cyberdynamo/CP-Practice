#Maximum Even Number

def fun1(string):
    lst=[]
    for i in string:
        if(i.isdigit()):
            lst.append(int(i))
    lst=list(set(lst))
    maxi=10
    for j in lst:
        if(j%2==0 and j<maxi):
            maxi=j
    if(maxi==10):
        return -1
    
    lst.remove(maxi)
    lst.sort(reverse=True)
    string=""
    for k in lst:
        string+=str(k)
    string+=str(maxi)
    return int(string)
    
string=input()
print(fun1(string))
