class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        min = nums[0]
        return min