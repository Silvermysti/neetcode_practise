class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        by_distance = sorted(arr, key=lambda y: abs(y-x))

        return(sorted(by_distance[:k]))
        