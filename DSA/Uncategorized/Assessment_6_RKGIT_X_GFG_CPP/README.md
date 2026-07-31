# Assessment 6 - RKGIT X GFG - CPP

Solved on **GFG** · Difficulty: **Unknown** · Category: **Uncategorized**

[View problem](https://practice.geeksforgeeks.org/contest/assessment-6-rkgit-x-gfg-cpp-5927/problems)

## Solution

```python
class Solution {
public:
vector<int> kLargest(vector<int>& arr, int k) {
// code here
vector<int> ans;
int n=arr.size();
sort(arr.begin(), arr.end());
reverse(arr.begin(),arr.end());
for(int i=0; i<k; i++){
ans.push_back(arr[i]);
}
return ans;
}
};
```
