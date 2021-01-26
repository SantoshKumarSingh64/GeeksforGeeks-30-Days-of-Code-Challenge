#User function Template for python3

class Solution:
    def prank(self, a, n): 
        #code here
        
        for x in range(n):
            a[x] += ((a[a[x]]%n)*n)
        
        for x in range(n):
            a[x] = a[x]//n
            
