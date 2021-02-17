class Solution:
    def shortestRange(self, root):
        # Return pair/tuple of range
        # Your code goes here
        def storein(root, lvl, lin, llv):
            if not root:
                return
            storein(root.left,lvl+1,lin,llv)
            lin.append(root.data)
            llv.append(lvl)
            storein(root.right,lvl+1,lin,llv)
    
    
        inorder=[]
        level=[]
        storein(root,0,inorder,level)
        
        i=j=k=cntzero=0
        maxDepth=max(level)+1
        depth=[0]*maxDepth
        for k in range(len(level)):
            depth[level[k]]+=1
            if level[k]==0:
                j=k
                break
        
        cntzero=depth.count(0)
        x,y=inorder[0],inorder[-1]
        if cntzero==0:
            x,y=inorder[i],inorder[j]
    
        while i<=k and j<len(inorder):
            while j<len(inorder):
                if cntzero==0:
                    if (y-x) > (inorder[j]-inorder[i]):
                        x,y=inorder[i],inorder[j]
                    break
                j+=1
    
                if j>= len(inorder):
                    break
                if depth[level[j]]==0:
                    cntzero-=1
                depth[level[j]]+=1
            
            while not cntzero and i<=k:
                if (y-x)>(inorder[j]-inorder[i]):
                    x,y=inorder[i],inorder[j]
                depth[level[i]]-=1
                if depth[level[i]]==0:
                    cntzero+=1
                i+=1
        
        return (x,y)
