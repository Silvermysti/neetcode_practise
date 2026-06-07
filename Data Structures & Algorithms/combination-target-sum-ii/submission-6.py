class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res=[]
        def search(candidates,arr,net):
            if net==target:
                self.res.append(arr.copy())
                return
            elif net>target:
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                search(candidates[i+1:],arr,net+candidates[i])
                arr.remove(candidates[i])
            
        search(sorted(candidates), [], 0)

        return self.res