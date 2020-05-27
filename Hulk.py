n=int(input())
string="I "
for i in range(1,n+1):
    if(i%2!=0):
        string+="hate "
    else:
        string+="love "

    if(i!=n):
        string+="that I "
string+="it"
print(string)
