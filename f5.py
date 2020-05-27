string=input()

for i in string:
    if(i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u" or i.lower()=="y"):
        string=string.replace(i,"")

lst=list(string)
lst2=[]
for i in lst:
    lst2.append(i.lower())
t=1
for i in range(1,len(lst2)):
    lst2.insert(t,".")
    t+=2
lst2.insert(0,".")

print("".join(lst2))
    
        
        
