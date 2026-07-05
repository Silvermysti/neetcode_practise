class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        maxdist={c:-1 for c in range(n)}
        graph=defaultdict(set)
        remain=set(range(n))
        leaf=set(range(n))

        for i,j in edges:
            if i in remain:
                remain.remove(i)
            elif i in leaf:
                leaf.remove(i)
            if j in remain:
                remain.remove(j)
            elif j in leaf:
                leaf.remove(j)
            
            graph[i].add(j)
            graph[j].add(i)
        #print(graph)
        
        #print(leaf)
        def dfs(node,dist,prev):
            #print(node,dist)
            maxdist[node]=max(maxdist[node],dist)
            #print(graph[node])
            for i in graph[node]:
                if i!=prev:
                    dfs(i,dist+1,node)
            return

        for node in leaf:
            dfs(node,0,None)
            #print("")
        #print(maxdist)

        mini=float('inf')
        minival=[]
        for node in maxdist:
            if mini>maxdist[node]:
                mini=maxdist[node]
                minival=[node]
            elif mini==maxdist[node]:
                minival.append(node)
        return minival
