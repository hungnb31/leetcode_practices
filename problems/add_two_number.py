# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        current = result
        carry = 0
        while(l1 or l2):
            x = l1.val if (l1 != None) else 0
            y = l2.val if (l2 != None) else 0
            sum = x + y + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        
        if (carry > 0):
            current.next = ListNode(carry)
        
        return result.next