class Solution:
    def numWays(self, s : str) -> int:
        # code here
        n=len(s)
        
        dp=[0]*n
        dp[0]=1
        for i in range(n):
            if dp[i]==0:
                continue
            
            if i+1<n:
                dp[i+1]=(dp[i+1]+dp[i])%(10**9 +7)
            if s[i]=='0' and i+2<n:
                dp[i+2]=(dp[i+2]+dp[i])%(10**9 +7)
        return dp[n-1]
