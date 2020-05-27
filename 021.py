string=input()
dic={}
string2=""
for i in range(len(string)):
    if(string[i].isalnum()==False):
        dic.update({i:string[i]})
    else:
        string2=string2+string[i]

string2=list(string2[::-1])
for i,j in dic.items():
    string2.insert(i,j)
print("".join(string2))

        
