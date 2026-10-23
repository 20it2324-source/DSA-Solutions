class Solution:
    def maxAND(self, arr):
        # code here
        ans=0
        
        for bit in range(31, -1,-1):
            candidate= ans | (1<<bit)
            
            count=0
            
            for num in arr:
                if (num & candidate)== candidate:
                    count+=1
                    
            if count >=2:
                ans= candidate
        return ans
