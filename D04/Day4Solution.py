class Solution:
    def find_min(self, a, n, k):
        #Code Here
        max_pair = 0
        total = 0
        
        for x in a:
            
            max_pair += (x//2)
            if x%2 == 0:
                total += (x-2)//2
            else:
                total += (x-1)//2
            
        if max_pair < k:
            return -1
            
        if total >= k:
            return 2*(k-1) + (n+1)
        
        return 2*total + n + (k-total) 
            
