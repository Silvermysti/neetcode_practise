class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        self.jumps=0

        while r<len(nums)-1:
            maxrange=0
            for i in range(l,r+1):
                maxrange=max(i+nums[i],maxrange)
            self.jumps+=1
            l=r+1
            r=maxrange
            print(l,r,self.jumps)
        
        return self.jumps
            
            