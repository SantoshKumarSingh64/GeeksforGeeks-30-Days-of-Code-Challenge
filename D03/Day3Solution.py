class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here 
        res = 1
        array.sort()
        x = 0
        while x < n and array[x] <= res:
            res += array[x]
            x += 1
        
        return res
