class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums)<target:
            return 0
        
        backward=0
        forward=0
        currsum=0
        minlen=float('inf')

        while forward<len(nums):
            currsum+=nums[forward]
            if currsum>=target:
                while currsum>=target and backward<=forward:
                    currsum-=nums[backward]
                    backward+=1
                if minlen>forward-backward+2:
                    minlen=forward-backward+2
            forward+=1
            #print(nums[backward-1:forward+1])
            #print(minlen)
        return minlen
        