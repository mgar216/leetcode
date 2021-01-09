'''
Runtime: 56 ms, faster than 25.47% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 98.72% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n, i in enumerate(nums):
            for p, x in enumerate(nums[1:], start=1):
                if (i + x) == target:
                    if n != p:
                        return [n, p]
