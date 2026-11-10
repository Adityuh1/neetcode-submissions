class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sortedN = sorted(nums)
        n = len(sortedN)
        return int(sortedN[n//2])

