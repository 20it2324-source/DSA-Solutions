# Remove Element

Solved on **LeetCode** · Difficulty: **Easy** · Category: **Arrays**

[View problem](https://leetcode.com/problems/remove-element/)

## Solution

```python
class Solution:
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
```
