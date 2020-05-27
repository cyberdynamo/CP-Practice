#longest prefix and suffix
s = input()
rev = s[::-1]
c=0
for i in range(len(s)):
    if s[i]==rev[i]:
        c+=1
    else:
        if i==0:
            c=-1
        break
print(c)
