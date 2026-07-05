class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        pairs=defaultdict(int)
        numerators=defaultdict(set)
        for i in range(len(equations)):
            pairs[(equations[i][0]),equations[i][1]]=values[i]
            pairs[(equations[i][1],equations[i][0])]=1/values[i]
            numerators[equations[i][0]].add(equations[i][1])
            numerators[equations[i][1]].add(equations[i][0])

        print(numerators)
        print(pairs)
        
        result=[]
        self.visited=set()

        def dfs(node,target):

            if node in self.visited:
                return -1
            
            self.visited.add(node)
            for i in numerators[node]:
                if i==target:
                    return pairs[(node,i)]
                res=dfs(i,target)
                if res!=-1:
                    #print(node,"/",i)
                    return pairs[(node,i)]*res
            return -1
        
        for numerator,denominator in queries:
            self.visited=set()
            result.append(dfs(numerator,denominator))
            #print("")
            #print("")

        return result