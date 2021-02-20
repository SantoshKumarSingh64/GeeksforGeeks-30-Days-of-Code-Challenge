class Solution:
    def findDistance(self, matrix, m, n):
        # Your code goes here
        
        mod = 10**9+7
        ans = [[mod for x in range(n)] for y in range(m)]
        vis = [[False for x in range(n)]for y in range(m)]
        q = []
        dx = [ -1 ,0 , 0, 1 ]
        dy = [0 ,-1, 1, 0 ]
        
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 'B':
                    ans[x][y] = 0
                    q.append([[x,y],0])
                    vis[x][y] = True
                if matrix[x][y] == 'W':
                    ans[x][y] = -1
        
        
        while len(q) > 0:
            
            p = q[0]
            q = q[1:]
            for i in range(4):
                                
                if p[0][0] + dx[i] >= 0 and p[0][1] + dy[i] >= 0 and p[0][0] + dx[i] <  m and p[0][1] + dy[i] < n and matrix[p[0][0]+dx[i]][p[0][1]+dy[i]] != 'W':
                    
                    if vis[p[0][0] + dx[i]][p[0][1]+dy[i]] == False:
                        z = [[p[0][0] + dx[i] , p[0][1] + dy[i]] , p[1]+1]
                        ans[p[0][0]+dx[i]][p[0][1]+dy[i]] = p[1] + 1
                        q.append(z)
                        vis[p[0][0] + dx[i]][p[0][1]+dy[i]] = True
                    
                    else:
                        ans[p[0][0]+dx[i]][p[0][1] + dy[i]] = min(ans[p[0][0]+dx[i]][p[0][1]+dy[i]],p[1]+1)
                        
        for x in range(m):
            for y in range(n):
                if ans[x][y] == mod:
                    ans[x][y] = -1
        
        return ans
