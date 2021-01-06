"""
Runtime: 48 ms, faster than 71.85% of Python3 online submissions for Search Insert Position.
Memory Usage: 15 MB, less than 44.17% of Python3 online submissions for Search Insert Position.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return [n for n, i in enumerate(nums) if i == target][0]
        else:
            nums.append(target)
            return [n for n, i in enumerate(sorted(nums)) if i == target][0]
