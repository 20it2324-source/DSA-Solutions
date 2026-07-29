# Two Sum

Solved on **LeetCode** · Difficulty: **Easy** · Category: **Arrays**

[View problem](https://leetcode.com/problems/two-sum/)

## Solution

```python
class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in mp:
                return [mp[complement], i]

            mp[nums[i]] = i
```
