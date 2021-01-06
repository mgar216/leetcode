"""
Runtime: 44 ms, faster than 90.68% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.1 MB, less than 18.16% of Python3 online submissions for Search Insert Position.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        return [n for n, i in enumerate(sorted(nums)) if i == target][0]
