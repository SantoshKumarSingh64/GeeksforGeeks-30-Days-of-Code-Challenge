class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        dp = [-1 for x in range(n)]
        
        for i in range(n):
            if gallery[i] != -1:
                right = min(i+gallery[i],n-1)
                left = max(0,i-gallery[i])
                dp[left] = max(dp[left],right)

        right = dp[0]
        next_index = -1
        ans = 1
        
        for i in range(n):
            
            next_index = max(next_index,dp[i])
            
            if i > right and next_index <= i-1:
                return -1
            
            if i == right+1:
                ans += 1
                right = next_index
        
        return ans
