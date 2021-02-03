import math
class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        ans = int(math.ceil(len(B)/len(A)))
        for i in range(2):
            if B in (A * (ans + i)):
                return ans + i
        return -1
