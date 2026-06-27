class Solution:
    def jump(self, nums: List[int]) -> int:
        length=len(nums)-1
        memo=defaultdict(int)

        def traverse(currind):

            if currind>=length:
                #print(self.mindis,currind)
                return 0
            if nums[currind]==0:
                return float('inf')
            if currind in memo:
                return memo[currind]

            best=float('inf')
            for i in range(1, nums[currind]+1):
                #print("traverse(",currind+i," , ",jumps+1," )")
                best=min(traverse(currind+i)+1,best)
            memo[currind]=best
            return best

        return traverse(0)
            
            