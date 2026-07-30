# Leaders In An Array

Solved on **GFG** · Difficulty: **Unknown** · Category: **Arrays**

[View problem](https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/)

## Solution

```python
class Solution:
def leaders(self, arr):
n = len(arr)
ans = []
max_right = arr[-1]
ans.append(max_right)
for i in range(n - 2, -1, -1):
if arr[i] >= max_right:
ans.append(arr[i])
max_right = arr[i]
return ans[::-1]
```
