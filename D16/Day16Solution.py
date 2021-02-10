class Solution:
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        if k == 1:
            return ""
        stack = []
        
        for x in s:
            if stack and stack[-1][0] == x:
                if stack[-1][1] == k-1:
                    while stack and stack[-1][0] == x:
                        stack.pop()
                else:
                    stack.append([x,stack[-1][1]+1])
            else:
                stack.append([x,1])
            
            
        return ''.join(x[0] for x in stack)
