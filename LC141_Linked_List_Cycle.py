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
