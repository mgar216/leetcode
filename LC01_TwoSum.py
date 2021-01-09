'''
Runtime: 56 ms, faster than 25.47% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 98.72% of Python3 online submissions for Two Sum.
O(n^2) - quadratic time complexity:
O(1) - Constant storage complexity:
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n, i in enumerate(nums):
            for p, x in enumerate(nums[1:], start=1):
                if (i + x) == target:
                    if n != p:
                        return [n, p]

'''
Runtime: 44 ms, faster than 85.71% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 24.62% of Python3 online submissions for Two Sum.
O(n) - Linear time complexity:
O(n) - Linear storage complexity:
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for n, i in enumerate(nums):
            spec = target - i
            if spec in storage:
                return [storage[spec], n]
            else:
                storage[i] = n
