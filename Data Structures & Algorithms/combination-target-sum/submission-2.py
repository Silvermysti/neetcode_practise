class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res=[]
        def search(start,arr,currsum):
            if currsum==target:
                self.res.append(arr.copy())
                return
            elif currsum>target:
                return

            for i in range(start,len(nums)):
                arr.append(nums[i])
                search(i,arr,currsum+nums[i])
                arr.pop()


        search(0,[],0)
        return self.res