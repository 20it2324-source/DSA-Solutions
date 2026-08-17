# Count Set Bits in 1 to n

Solved on **GFG** · Difficulty: **Basic** · Category: **Bit Manipulation**

[View problem](https://www.geeksforgeeks.org/batch/dsa-cpp-rkgit/track/bitmagic-dsa-cpp-rkgit/problem/count-total-set-bits-1587115620)

## Solution

```python
class Solution:
    def countSetBits(self,n):
        # code here
        count=0
        i=0
        
        while(1<<i) <=n:
            c_len=1<<(i+1)
            f_cycle=(n+1)// c_len
            count+=f_cycle*(1<<i)
            
            rem=(n+1) % c_len
            count+=max(0, rem -(1<<i))
            i+=1
        return count
```
