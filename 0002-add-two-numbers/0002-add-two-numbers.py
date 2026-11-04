# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t1=l1
        t2=l2
        dummy=ListNode(-1)
        curr=dummy
        carry=0
        while t1 or t2:
            total=carry
            if t1:
                total=total+t1.val
                t1=t1.next
            if t2:
                total=total+t2.val
                t2=t2.next
            newnode=ListNode(total%10)
            carry=total//10
            curr.next=newnode
            curr=curr.next
            if carry:
                newnode=ListNode(carry)
                curr.next=newnode
        return dummy.next

        