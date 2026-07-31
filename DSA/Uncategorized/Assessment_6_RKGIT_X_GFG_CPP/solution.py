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
