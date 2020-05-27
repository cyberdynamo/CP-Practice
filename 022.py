string1=input()
string2=input()
l1=len(string1)
l2=len(string2)
string=string1+string2
def swap(string,i,j):
    return (string[:i]+string[j]+string[i+1:j]+string[i]+string[j+1:])
def MakeNumber(string,l1,l2):
    str1=""
    str2=""
    for i in range(l1):
        str1+=string[i]
    for i in range(l1,l1+l2):
        str2+=string[i]
    s=int(str1)+int(str2)
    return s

lst=[]
for i in range(len(string1)):
    for j in range(l1,l1+l2):
        stringh=swap(string,i,j)
        lst.append(MakeNumber(stringh,l1,l2))
print(lst)
print(max(lst))




