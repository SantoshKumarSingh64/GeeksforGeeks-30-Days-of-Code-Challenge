class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stack = []
        ans = []
        
        for x in arr[::-1]:
            while stack and stack[-1] >= x:
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(x)
        
        return ans[::-1]
