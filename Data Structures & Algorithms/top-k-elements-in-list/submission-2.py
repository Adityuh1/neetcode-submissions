class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # Sort the items by frequency (value) in descending order
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        result = []
        # Take the keys of the first k elements from the sorted list
        for i in range(k):
            result.append(sorted_items[i][0])
        return result