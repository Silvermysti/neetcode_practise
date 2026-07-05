class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        graph=defaultdict(set)
        visited=set()
        cycle=set()
        cyclesets=set()
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        self.cycle=1
        res=set()
        self.found=-1
        def dfs(node, prev):
            if node in visited:
                self.cycle=0
                self.found=node
                res.add((node,prev))
                return True
            
            visited.add(node)
            for i in graph[node]:
                if i!=prev and dfs(i,node):
                    if node!=self.found and self.cycle==0:
                        res.add((node,prev))
                    elif node==self.found:
                        cycle==1
                    return True
                    break
            return False

        dfs(1,None)
        
        for i,j in edges[::-1]:
            #print(i,j,res)
            if (i,j) in res or (j,i) in res:
                return [i,j]


            
