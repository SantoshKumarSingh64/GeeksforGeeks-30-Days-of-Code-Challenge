class Solution:
    def transfigure(self, A, B): 
        # code here 
        
        length_A = len(A)
        length_B = len(B)
        
        if length_A != length_B:
            return -1
        
        arr = [0]*256
        
        for x in range(length_A):
            arr[ord(B[x])] += 1
        for x in range(length_A):
            arr[ord(A[x])] -= 1
            
        for x in range(256):
            if arr[x]:
                return -1
        
        index_A = length_A-1
        index_B = index_A
        ans = 0
        
        while index_A >= 0:
            
            while index_A >= 0 and A[index_A] != B[index_B]:
                index_A -= 1
                ans += 1
            
            if index_A >= 0:
                index_A -= 1
                index_B -= 1
        
        return ans
