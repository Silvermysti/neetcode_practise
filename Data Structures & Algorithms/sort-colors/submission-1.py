class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        count2=0

        for i in nums:
            if i==1:
                count1+=1
            elif i==2:
                count2+=1
            else:
                count0+=1
    
        nums[:count0]=[0]*count0
        nums[count0:count1+count0]=[1]*count1
        nums[count0+count1:]=[2]*count2


        