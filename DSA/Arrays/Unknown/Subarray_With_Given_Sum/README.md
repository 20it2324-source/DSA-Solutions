# Subarray With Given Sum

Solved on **GFG** · Difficulty: **Unknown** · Category: **Arrays**

[View problem](https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/)

## Solution

```python
class Solution:
def subarraySum(self, arr, target):
start = 0
curr_sum = 0
for end in range(len(arr)):
curr_sum += arr[end]
while curr_sum > target:
curr_sum -= arr[start]
start += 1
if curr_sum == target:
return [start+1, end+1]
return [-1]
```
