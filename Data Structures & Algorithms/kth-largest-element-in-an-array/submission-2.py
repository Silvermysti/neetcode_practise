class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        K=-1
        while K<k:
            heapq.heappop(nums)
            K+=1

        return heapq.heappop(nums)