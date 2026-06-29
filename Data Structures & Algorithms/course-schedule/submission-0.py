class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        self.cyclefound=False
        graph=defaultdict(set)
        for i,j in prerequisites:
            if (j not in graph) or (i not in graph[j]):
                graph[i].add(j)
            else:
                return False
        #print(graph)

        visited=set()
        traversed=set()

        def traverse(node):
            traversed.add(node)
            if node in graph:
                for i in graph[node]:
                    if i in visited:
                        self.cyclefound=True
                    visited.add(i)
                    traverse(i)
                    visited.remove(i)

        for node in graph.keys():
            if node not in traversed:
                visited.add(node)
                traverse(node)
                visited.add(node)
                
        if self.cyclefound==True:
            return False
        return True
