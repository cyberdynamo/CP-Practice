def fun1(string):
    string=list(set(string))
    maxi=10
    for i in string:
        if(int(i)%2==0 and int(i)<maxi):
            maxi=int(i)
    if(maxi==10):
        return -1
    else:
        string.remove(str(maxi))
        string.sort(reverse=True)
        string2="".join(string)
        string2+=str(maxi)
        return int(string2)

string=input()
lst=[]
for i in string:
    if(i.isdigit()==True):
        lst.append(i)
print(fun1(lst))
