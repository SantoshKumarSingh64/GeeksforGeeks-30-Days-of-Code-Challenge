class Solution:
    def Kclosest(self, arr, n, x, k):
        # Your code goes here
        def findX(arr, low, high, x) :  
          
            if (arr[high] <= x) : # x is greater than all  
                return high 
                  
            if (arr[low] > x) : # x is smaller than all  
                return low  
              
            mid = (low + high) // 2 # low + (high - low)// 2  
              
            if (arr[mid] <= x and arr[mid + 1] > x) : 
                return mid  
              
            if(arr[mid] < x) : 
                return findX(arr, mid + 1, high, x) 
              
            return findX(arr, low, mid - 1, x)             
        
        arr.sort()
        l = findX(arr, 0, n - 1, x) 
        r = l + 1
        count = 0  
      
        while (l >= 0 and r < n and count < k) : 
              
            if (x - arr[l]) <= (arr[r] - x) :
                l -= 1
            elif (x - arr[l]) > (arr[r] - x):
                r += 1
                
            count += 1
      
        while (count < k and l >= 0):
            l -= 1
            count += 1
      
        while (count < k and r < n) :
            r += 1
            count += 1
    
        if l == -1:
            return arr[:r]
        return arr[l+1:r]
