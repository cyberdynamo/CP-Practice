lst=input().split(",")
def Rotate(string, number):
    s=0
    string=list(string)
    for i in number:
        s=s+((int(i))**2)
    if(s%2==0):
        string=string[-1:]+string[:-1]
    else:
        string=string[2:]+string[:2]
     return string   

for i in lst:
    string,number=i.split(":")
    print(Rotate(string,number))
