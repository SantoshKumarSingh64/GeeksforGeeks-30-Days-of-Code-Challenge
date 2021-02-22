class Solution:
    def catchThieves(self, arr, n, k): 
        # code here 
        police = []
        police_length = 0
        theif = []
        theif_length = 0
        
        for x in range(n):
            if arr[x] == 'P':
                police.append(x)
                police_length += 1
            else:
                theif.append(x)
                theif_length += 1
        
        police_pos = 0
        theif_pos = 0
        ans = 0
        
        while police_pos < police_length and theif_pos < theif_length:
            
            if abs(police[police_pos] - theif[theif_pos]) <= k:
                ans += 1
                police_pos += 1
                theif_pos += 1
            
            elif police[police_pos] < theif[theif_pos]:
                police_pos += 1
            
            else:
                theif_pos += 1
        
        return ans
