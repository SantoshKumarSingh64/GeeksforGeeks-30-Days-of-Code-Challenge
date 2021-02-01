class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
        ans = 0
        low = 0
        high = n-1
        
        while low < high:
            
            if height[low] <= height[high]:
                ans = max(ans,height[low]*(high-low-1))
                low += 1
            else:
                ans = max(ans,height[high]*(high-low-1))
                high -= 1
        
        return ans
