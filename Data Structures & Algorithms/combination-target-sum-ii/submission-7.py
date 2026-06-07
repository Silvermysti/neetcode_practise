class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res=[]
        def search(start,arr,net):
            if net==target:
                self.res.append(arr.copy())
                return
            elif net>target:
                return

            for i in range(start,len(candidates)):
                if i==2:
                    print(i)
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                search(i+1,arr,net+candidates[i])
                arr.remove(candidates[i])
        
        candidates=sorted(candidates)
        search(0, [], 0)

        return self.res