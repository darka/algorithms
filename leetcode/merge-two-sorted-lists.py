# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        # Merge l2 into l1 but make sure l1 starts with smaller value
        if l1.val > l2.val:
            tmp = l1
            l1 = l2
            l2 = tmp
        
        ret = l1
        
        while l1:
            if l1.next:
                if l2 and l1.next.val > l2.val:
                    tmp = l2.next
                    l2.next = l1.next
                    l1.next = l2
                    l2 = tmp
                l1 = l1.next
            else:
                l1.next = l2
                break
        
        return ret
