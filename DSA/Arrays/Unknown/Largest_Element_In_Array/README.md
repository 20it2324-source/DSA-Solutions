# Largest Element In Array

Solved on **GFG** · Difficulty: **Unknown** · Category: **Arrays**

[View problem](https://www.geeksforgeeks.org/problems/largest-element-in-array4009/)

## Solution

```python
class Solution:
def largest(self, arr):
# code here
maxi=0
for num in arr:
if num>maxi:
maxi=max(num,maxi)
return maxi
```
