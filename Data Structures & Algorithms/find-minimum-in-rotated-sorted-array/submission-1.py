class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_map = {}
        for i,j in enumerate(nums):
            nums_map[i] = j
        print(nums_map)

        min_value = min(nums_map.values())
        return min_value