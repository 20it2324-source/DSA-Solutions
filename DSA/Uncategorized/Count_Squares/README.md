# Count Squares

Solved on **GFG** · Difficulty: **Unknown** · Category: **Uncategorized**

[View problem](https://www.geeksforgeeks.org/problems/count-squares3649/)

## Solution

```python
class Solution:
    def countSquares(self, n):
        i = 1
        count = 0

        while i * i < n:
            count += 1
            i += 1
```
