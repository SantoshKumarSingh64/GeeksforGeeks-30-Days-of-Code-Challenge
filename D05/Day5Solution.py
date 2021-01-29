class Solution:
    def findK(self, a, n, m, k):
        # Your code goes here
        left,up = 0,0
        right,down = m-1,n-1

        case = 0
        ans = []

        while left <= right and up <= down:

            if case == 0:
                for x in range(left,right+1):
                    k -= 1
                    if k == 0:
                        return a[up][x]
                up +=1

            elif case == 1:
                for x in range(up,down+1):
                    k -= 1
                    if k == 0:
                        return a[x][right]
                right -= 1

            elif case == 2:
                for x in range(right,left-1,-1):
                    k -= 1
                    if k == 0:
                        return a[down][x]
                down -= 1

            else:
                for x in range(down,up-1,-1):
                    k -= 1
                    if k == 0:
                        return a[x][left]
                left += 1

            case  = (case+1)%4
