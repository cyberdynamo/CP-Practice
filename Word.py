word=input()
c1=0
c2=0
for i in range(len(word)):
    if(word[i].isupper()==True):
        c1+=1
    else:
        c2+=1
if(c2>=c1):
    print(word.lower())
else:
    print(word.upper())
