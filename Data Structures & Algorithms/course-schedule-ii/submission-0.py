class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq={c:set() for c in range(numCourses)}
        cycle=set()
        visited=set()
        res=[]

        for i in prerequisites:
            prereq[i[0]].add(i[1])
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            for j in prereq[node]:
                if dfs(j)==False:
                    return False
            cycle.remove(node)
            visited.add(node)
            #print(node)
            res.append(node)


        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return res


            
