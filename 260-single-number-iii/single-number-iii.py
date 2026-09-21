class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        return [num for num, count in freq.items() if count == 1]
