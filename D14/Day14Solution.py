class Solution:    
    def RulingPair(self, arr, n): 
    	# Your code goes here
        def findSum(x):
                temp = 0
                while x > 0:
                        temp += x%10
                        x = x//10
                return temp
                
        
        dt = {}
        ans = -1
        arr.sort()
        for x in arr:
                digitsum = findSum(x)
            
                if digitsum in dt:
                        ans = max(ans,x+dt[digitsum][-1])
                else:
                        dt[digitsum] = []
                dt[digitsum].append(x)
        return ans
