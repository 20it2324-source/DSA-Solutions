class Solution:
    def isPowerofTwo(self, n):
        # code here
    
        if n & (n-1) == 0:
            return True
        else:
            return False
