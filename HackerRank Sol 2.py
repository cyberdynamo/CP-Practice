def function1(A):
    lst=[1,2,3]
    lst.append(5)
    lst.append(4)
    if(len(A)<2):
        return len(A)
    best,Lower,Higher=1,1,1
    for i in range(1,len(A)):
        if(A[i]==A[i-1]):
          Lower+=1
          Higher+=1
        elif(A[i]-1==A[i-1]):
          Lower=1+Higher
          Higher=1
        elif(A[i] + 1 == A[i-1]):
          Higher=Lower+1
          Lower=1
        else:
          Lower=1
          Higher=1
        best=max(best,Lower,Higher)
    return best

n=int(input())
A=[]
for j in range(n):
    A.append(int(input()))
print(function1(A))
