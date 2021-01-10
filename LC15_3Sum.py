'''
Runtime: 4392 ms, faster than 7.22% of Python3 online submissions for 3Sum.
Memory Usage: 17.5 MB, less than 48.86% of Python3 online submissions for 3Sum.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        b = 1
        c = len(nums)-1
        b_o = 1
        c_o = len(nums)-1
        storage = []
        nums = sorted(nums)
        for i in nums:
            if i > 0: continue
            while b < c:
                sumtotal = i + nums[b] + nums[c]
                if sumtotal < 0:
                    b = b + 1
                elif sumtotal > 0:
                    c = c - 1
                elif sumtotal == 0:
                    if [i, nums[b], nums[c]] not in storage:
                        storage.append([i, nums[b], nums[c]])
                    b = b + 1
                    c = c - 1
            b_o = b_o + 1
            b, c = b_o, c_o
        return storage
