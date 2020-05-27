# Python program for the above approach 
import math 

# Function to check 
# palindrome
def Digit(i):
    temp=i
    while(i!=0):
        d=i%10
        if(d==0):
            return False
        i=i//10
    return True
        
def isPalindrome(s): 
	left = 0
	right = len(s) - 1
	while (left <= right): 
		if (s[left] != s[right]): 
			return False
		
		left = left + 1
		right = right - 1

	return True

# Function to calculate 
# the sum of n-digit 
# palindrome 
def getSum(n): 
	start = int(math.pow(10, n - 1)) 
	end = int(math.pow(10, n)) - 1

	sum = 0

	# Run a loop to check 
	# all possible palindrome 
	for i in range(start, end + 1): 
		s = str(i) 
		
		# If palndrome 
		# append sum 
		if (isPalindrome(s) and (i%9==0) and Digit(i)): 
			sum = sum + i 

	return sum

# Driver code 

n = 8
ans = getSum(n) 
print(ans) 

# This code is contributed by Sanjit_Prasad 
