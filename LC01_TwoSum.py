'''
Runtime: 52 ms, faster than 31.61% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 92.02% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n, i in enumerate(nums):
            for p, x in enumerate(nums[1:], start=1):
                if (i + x) == target:
                    if n != p:
                        return [n, p]
