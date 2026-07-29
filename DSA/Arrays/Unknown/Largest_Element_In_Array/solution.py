class Solution:
def largest(self, arr):
# code here
maxi=0
for num in arr:
if num>maxi:
maxi=max(num,maxi)
return maxi
