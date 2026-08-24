# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            copy = curr.next
            curr.next = prev
            prev = curr
            curr = copy

        return prev





    """
    OPTIMAL ITERATIVE SOLUTION (O(n) time and O(1) space)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        return prev


    
    OPTIMAL RECURSIVE SOLUTION (O(N) time and space):

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
        
    """


