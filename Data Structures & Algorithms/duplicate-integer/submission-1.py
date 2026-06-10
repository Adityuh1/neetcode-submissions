class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = Counter(nums)
        for count in nums_map.values():
            if count > 1:
                return True
        return False