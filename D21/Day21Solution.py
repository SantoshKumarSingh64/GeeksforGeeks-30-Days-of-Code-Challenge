class Solution:
    def supplyVaccine(self, root):
        # Your code goes here
        
        def dfs(node1,node2):
            if node1 != None:
                dfs(node1.left,node1)
                dfs(node1.right,node1)
                
                if node2 == None and not covered.get(node1,False) or not covered.get(node1.left,False) or not covered.get(node1.right,False):
                    self.result += 1
                    covered[node1] = True
                    covered[node2] = True
                    covered[node1.left] = True
                    covered[node1.right] = True
        
        self.result = 0
        covered = {}
        covered[None] = True
        dfs(root,None)
        return self.result
