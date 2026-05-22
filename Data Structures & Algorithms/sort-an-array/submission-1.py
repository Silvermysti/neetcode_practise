class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        temp=None
        leastInd=None
        least=None

        for i in range(len(nums)):

            for j in range(i,len(nums)):
                if (least==None or nums[j]<least):
                    least=nums[j]
                    leastInd=j

            temp=nums[leastInd]
            nums[leastInd]=nums[i]
            nums[i]=temp
            least=None

        return nums