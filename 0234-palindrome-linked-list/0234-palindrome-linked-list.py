# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        while slow:
            nextnode=slow.next
            slow.next = prev
            prev=slow
            slow=nextnode
        while prev:
            if prev.val!=head.val: 
                return False
            head=head.next
            prev=prev.next    
                
        return True