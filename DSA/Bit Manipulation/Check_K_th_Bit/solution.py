class Solution:
    def checkKthBit(self, n, k):
        # code here
        for k in range(n):
            
            return (n>>k) & 1
