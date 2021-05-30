# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = ListNode()
        print(curr.next)
        print(curr.val)
        curr.next = head
        length = 0
        first = head
        # loop through the list and find out the length of the list
        while (first):
            length += 1
            first = first.next

        length -= n
        first = curr
        while(length > 0):
            length -= 1
            first = first.next

        first.next = first.next.next
        return curr.next
