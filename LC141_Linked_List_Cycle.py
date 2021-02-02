"""
Runtime: 64 ms, faster than 16.24% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.5 MB, less than 12.03% of Python3 online submissions for Linked List Cycle.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        location = set()
        on = head
        while on:
            if on in location:
                return True
            location.add(on)
            on = on.next
        return False

"""
Runtime: 44 ms, faster than 89.89% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.2 MB, less than 67.21% of Python3 online submissions for Linked List Cycle.
Uses Floyd's Tortoise and Hare algorithm (Cycle detection algorithm) to detect cycles—keeps O(1) space complexity.
https://en.wikipedia.org/wiki/Cycle_detection
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        on = head
        f = head
        while f:
            try:
                f = f.next.next
            except AttributeError:
                return False
            on = on.next
            if on == f:
                return True
        return False
