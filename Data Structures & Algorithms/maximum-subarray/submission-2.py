class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        res=nums[0]
        currsum=nums[0]

        for i in range(1,len(nums)):
            
            if nums[i]<0:
                res=max(res,currsum)
            if currsum<0:
                currsum=nums[i]
            else:
                currsum+=nums[i]
            #print(currsum, nums[i])

        res=max(res,currsum)
        
        return res