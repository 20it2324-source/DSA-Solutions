# Power of 2

Solved on **GFG** · Difficulty: **Basic** · Category: **Uncategorized**

[View problem](https://www.geeksforgeeks.org/batch/dsa-cpp-rkgit/track/bitmagic-dsa-cpp-rkgit/problem/power-of-2-1587115620)

## Solution

```python
class Solution:
    def isPowerofTwo(self, n):
        # code here
    
        if n> 0 and (n & (n-1)) == 0:
            return True
        else:
            return False
```
