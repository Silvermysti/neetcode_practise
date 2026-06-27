class Solution:
    def jump(self, nums: List[int]) -> int:
        
        self.mindis=1000
        length=len(nums)-1


        def traverse(currind,jumps):

            if currind>=length:
                self.mindis=min(self.mindis,jumps)
                #print(self.mindis,currind)
                return

            for i in range(1, nums[currind]+1):
                #print("traverse(",currind+i," , ",jumps+1," )")
                traverse(currind+i,jumps+1)
        

        traverse(0,0)

        return self.mindis
            
            