# Maximum AND Value

Solved on **GFG** · Difficulty: **Basic** · Category: **Uncategorized**

[View problem](https://www.geeksforgeeks.org/batch/dsa-cpp-rkgit/track/bitmagic-dsa-cpp-rkgit/problem/maximum-and-value-1587115620)

## Solution

```python
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
```
