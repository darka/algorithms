# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return
        
        prev = head
        current = head.next
        
        while current:
            if current.val == prev.val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        
        return head
