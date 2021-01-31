"""
Runtime: 128 ms, faster than 10.38% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.3 MB, less than 12.02% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        items = sorted(intervals)
        inventory = []
        while items:
            if not inventory:
                inventory.append(items.pop(0))
            try:
                next = items.pop(0)
            except IndexError:
                return inventory
            if inventory[-1][0] < next[0] and inventory[-1][1] > next[1]:
                continue
            elif inventory[-1][1] >= next[0]:
                new = (inventory.pop()[0], next[1])
                inventory.append(new)
            else:
                inventory.append(next)
        return inventory
