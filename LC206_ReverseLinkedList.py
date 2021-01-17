"""
Runtime: 36 ms, faster than 66.61% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 48.63% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        on = head
        prevNode = None
        while on:
            nextNode = on.next
            on.next = prevNode
            prevNode = on
            on = nextNode
        return prevNode
