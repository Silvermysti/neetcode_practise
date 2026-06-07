class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res=[]
        self.counts=[]
        def search(nums,arr,currsum):
            if currsum==target:
                counts=Counter(arr)
                if counts not in self.counts:
                    self.res.append(arr.copy())
                    self.counts.append(counts.copy())
                return
            elif currsum>target:
                return

            for i in nums:
                arr.append(i)
                search(nums,arr,currsum+i)
                arr.pop()


        search(nums,[],0)
        return self.res