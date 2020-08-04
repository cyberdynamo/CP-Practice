lst=list(map(int,input().split(",")))
sum1=sum(lst[:lst.index(5)])+sum(lst[lst.index(8)+1:])
lst2=lst[lst.index(5):lst.index(8)+1]
lst2=list(map(str,lst2))
string="".join(lst2)
print(sum1+int(string))
