import operator
class Solution:
    def TopK(self, array, k):
        # code here
        dt = {}
        for x in array:
            dt[x] = dt.get(x,0)+1
            
        dt_1 = {}    
        for x in dt.keys():
            if dt[x] not in dt_1:
                dt_1[dt[x]] = []
            dt_1[dt[x]].append(x)
        
        
        arr = sorted(list(dt_1.items()), key=operator.itemgetter(0),reverse=True)
        ans = []
        
        count = 0
        for x in arr:
            x[1].sort(reverse = True)
            for item in x[1]:
                if count == k:
                    return ans
                ans.append(item)
                count += 1
        
        return ans
