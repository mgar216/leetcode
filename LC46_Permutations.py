"""
Runtime: 92 ms, faster than 5.96% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 99.69% of Python3 online submissions for Permutations.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            container = []
            for i in range(len(nums)):
                temp = nums[i]
                remnants = nums[:i] + nums[i+1:]
                
                for p in self.permute(remnants):
                    container.append([temp] + p)     
        return container
