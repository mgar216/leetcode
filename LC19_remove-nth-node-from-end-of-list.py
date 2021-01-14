"""
Runtime: 28 ms, faster than 92.94% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.2 MB, less than 47.61% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        on = head
        length = 1
        while on:
            on = on.next
            length+=1
        leftIndex = length - n - 1
        if leftIndex == 0:
            return head.next
        on = head
        while leftIndex > 1:
            leftIndex -= 1
            on = on.next
        on.next = on.next.next
        return head
        
