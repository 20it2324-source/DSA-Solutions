# All Subsequences of String

Solved on **GFG** · Difficulty: **Basic** · Category: **Strings**

[View problem](https://www.geeksforgeeks.org/batch/dsa-cpp-rkgit/track/bitmagic-dsa-cpp-rkgit/problem/power-set4302)

## Solution

```python
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
```
