# Second Largest

Solved on **GFG** · Difficulty: **Unknown** · Category: **Uncategorized**

[View problem](https://www.geeksforgeeks.org/problems/second-largest3735/)

## Solution

```python
class Solution {
    public int getSecondLargest(int[] arr) {
        // code here
        //method-1
        /*int len=arr.length;
        int fl=0;
        for(int i:arr)
        {
            if(i>fl)
            {
                fl=i;
            }
        }
        int ans=0;
        int sl=0;
        for(int i:arr)
        {
            if(i<fl && i>ans)
            {
                sl=i;
                ans=sl;
            }
        }
        if(sl!=0)
        {
            return sl;
        }
        else
        {
            return -1;
        }*/
        //method-2
        int len=arr.length;
        int fl=0;
        int sl=0;
        for(int i:arr)
        {
            if(i>fl)
            {

                sl=fl;
                fl=i;
            }
            else if(i<fl && i>sl)
            {
                sl=i;
            }
        }
        if(sl!=0)
        {
            return sl;
        }
        else
        {
            return -1;
        }
    }
}
```
