test=int(input())
for t in range(test):
    s=input()
    c=0
    string=""
    lst=["a","e","i","o","u"]
    for i in s:
        if(i in lst):
            string+="0"
        else:
            string+="1"
    decimal = 0
    for digit in string:
        decimal = decimal*2 + int(digit)
    print(decimal%(10**9+7))
