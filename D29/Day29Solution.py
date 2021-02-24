class Solution:
    def maxFrequency(self, S):
        # code here
        length = len(S)
        
        i = 0
        j = length-1
        
        while i < length:
            if S[:i+1] == S[j:]:
                break
            i += 1
            j -= 1
        
        if i == length:
            return
        prefix = S[:i+1]
        
        return S.count(prefix)
