class Solution:
    def ValidPair(self, a, n): 
    	# Your code goes here
    	a.sort()
    	low = 0
    	high = n-1
    	count = 0
    	while low < high:
    	    if a[low]+a[high] <= 0:
    	        low += 1
    	    else:
    	        count += (high-low)
    	        high -= 1
    	return count
