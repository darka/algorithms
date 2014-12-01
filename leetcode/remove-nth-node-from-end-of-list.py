# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        ret = head
        current = head
        
        for i in xrange(n+1):
            if head == None and i == n:
                # Remove the first element
                return current.next
            head = head.next
            
        while head != None:
            head = head.next
            current = current.next
            
        current.next = current.next.next
        return ret
