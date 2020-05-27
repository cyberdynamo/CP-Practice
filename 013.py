#Maximum Even Number
def MaximumEvenNumber(string):
    lst=list(string)
    lst=list(set(lst))
    lst2=[]
    for i in lst:
        if(i.isdigit()):
            lst2.append(int(i))
    MAX=10
    for i in lst2:
        if(i%2==0 and i<MAX):
            MAX=i
    if(MAX==10):
        return -1

    lst2.remove(MAX)
    lst2.sort()

    lst2=list(map(str,lst2))
    s2="".join(lst2)+str(MAX)
    return s2
    
s1=input()
MaximumEvenNumber(s1)
