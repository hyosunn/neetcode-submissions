# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        copy = head
        if not copy or not copy.next:
            return False

        l, r = copy, copy.next.next
        while True:
            if not r or not r.next:
                return False
            elif l == r:
                return True
            l = l.next
            r = r.next.next
