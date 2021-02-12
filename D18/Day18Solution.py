class Solution:
	def recreationalSpot(self, arr, n):
		# Your code goes here 
		stack = []
		
		for x in arr:
		    if stack:
		        if stack[-1] > x:
		            if len(stack) >= 2 and stack[-2] < x:
		                return True
		            stack = []
		            stack.append(x)
		        else:
		            if stack[-1] < x and len(stack) > 1:
		                stack.pop()
		                stack.append(x)
		            else:
		                stack.append(x)
		    else:
		        stack.append(x)
	    
	    if len(stack) >= 2 and stack[-2] < x and stack[-1] > x:
	            return True
	    return False
