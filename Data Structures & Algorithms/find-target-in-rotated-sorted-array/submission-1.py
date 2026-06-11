class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_map = {}
        for i, j in enumerate(nums):
            nums_map[j] = i
        if target in nums_map:
            return nums_map[target]
        return -1

        