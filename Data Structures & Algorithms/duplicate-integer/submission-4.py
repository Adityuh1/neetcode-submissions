class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        if len(nums) != len(freq):
            return True
        else:
            return False
            