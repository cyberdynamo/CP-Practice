import math
inc = 1
word=list(map(int,input().split()))
print(math.ceil(len(word)/2)-1)
for i in range(math.ceil(len(word)/2) - 1,-1,-1):
    word[i] += inc 
    inc = word[i]//10
    word[i] %= 10
print(word)
