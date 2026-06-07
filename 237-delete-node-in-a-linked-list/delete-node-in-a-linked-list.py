# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node

        while curr.next :
            curr.val = curr.next.val
            if not curr.next.next :
                curr.next = curr.next.next
            else :
                curr = curr.next



        return 