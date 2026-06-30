class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

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
                        return True
                    visited.add(i)
                    if traverse(i):
                        return True
                    visited.remove(i)
            return False

        for node in graph.keys():
            if node not in traversed:
                visited.add(node)
                if traverse(node):
                    return False
                visited.add(node)
        return True
