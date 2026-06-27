class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target=len(nums)-1
        visited=set()

        def jump(currind):

            #print(currind)
            if currind==target or currind>target :
                return True
            elif nums[currind]==0:
                #print(" ")
                return False
            
            
            visited.add(currind)

            for i in range(1,nums[currind]+1):
                #print(i)
                if (currind+i not in visited) and jump(currind+i):
                    return True
            return False

        return jump(0)
