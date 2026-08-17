class Solution:
    def func(self,curr,ans,adj,visited):
        visited[curr]=True
        ans.append(curr)
        
        for neigh in adj[curr]:
            
            
            if not visited[neigh]:
                self.func(neigh,ans,adj,visited)
                
    def dfs(self, adj):
        # code here
        ans=[]
        visited=[False]*len(adj)
        self.func(0,ans,adj,visited)
        return ans
