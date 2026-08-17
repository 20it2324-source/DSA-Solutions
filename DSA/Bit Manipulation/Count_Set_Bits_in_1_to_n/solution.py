class Solution:
    def countSetBits(self,n):
        # code here
        count=0
        i=0
        
        while(1<<i) <=n:
            c_len=1<<(i+1)
            f_cycle=(n+1)// c_len
            count+=f_cycle*(1<<i)
            
            rem=(n+1) % c_len
            count+=max(0, rem -(1<<i))
            i+=1
        return count
