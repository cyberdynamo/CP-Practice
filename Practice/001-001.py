lst=list(map(int,input().split(",")))
num1=sum(lst[:lst.index(5)])+sum(lst[lst.index(8)+1:])
tmplst=lst[lst.index(5):lst.index(8)+1]
string=""
for i in tmplst:
    string+=str(i)
num2=int(string)
print(num1,num2)
