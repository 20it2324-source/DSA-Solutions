# Check K-th Bit

Solved on **GFG** · Difficulty: **Basic** · Category: **Bit Manipulation**

[View problem](https://www.geeksforgeeks.org/batch/dsa-cpp-rkgit/track/bitmagic-dsa-cpp-rkgit/problem/check-whether-k-th-bit-is-set-or-not-1587115620)

## Solution

```python
class Solution:
    def checkKthBit(self, n, k):
        # code here
        for k in range(n):
            
            return (n>>k) & 1
```
