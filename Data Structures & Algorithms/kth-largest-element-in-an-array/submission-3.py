class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        length=len(nums)
        while length>k:
            heapq.heappop(nums)
            length-=1

        return heapq.heappop(nums)