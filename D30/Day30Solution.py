class Solution:
    def build_bridges(self, str1, str2):
        # code here
        def longestCommonSubsequence(a,b,memo={}):
        
            key = a+","+b
        
            if key in memo:
                return memo[key]
            
            if len(a) == 0 or len(b) == 0:
                memo[key] = 0
                return memo[key]
        
            if a[0] == b[0]:
                ans = 1+longestCommonSubsequence(a[1:],b[1:],memo)
            else:
                left = longestCommonSubsequence(a[1:],b,memo)
                right = longestCommonSubsequence(a,b[1:],memo)
        
                ans = max(left,right)
        
            memo[key] = ans
            return memo[key]
        
        return longestCommonSubsequence(str1,str2)
