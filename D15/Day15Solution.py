def countTriplets(head,x):
    # code here
    
    def search(start,end,target,arr):
        
        while start <= end:
                mid = (start+end)//2
                if arr[mid] == target:
                        return True
                if arr[mid] > target:
                        start = mid+1
                else:
                        end = mid-1
        return False
    
    arr = []
    while head:
        arr.append(head.val)
        head = head.nxt
    left = 0
    n = len(arr)
    count = 0
    while left < n:
        for right in range(n-1,left+1,-1):
            if arr[left]+arr[right] < x and search(left+1, right-1, x - arr[left] - arr[right],arr):
                count += 1
        left += 1
    return count
