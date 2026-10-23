class Solution:
    def powerSet(self, s):
        # Code here
        res=[]
        def backtrack(i, curr):
            if i ==len(s):
                res.append(curr)
                return 
            
            backtrack(i+1, curr+ s[i])
            
            backtrack(i+1, curr)
        backtrack(0, "")
        
        res.sort()
        return res
