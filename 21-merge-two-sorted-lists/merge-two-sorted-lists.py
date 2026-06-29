# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        ans = ListNode(-1)
        currans = ans
        while curr1 and curr2 :
            if curr1.val < curr2.val :
                currans.next = ListNode(curr1.val)
                curr1 = curr1.next
                currans = currans.next
            else :
                currans.next = ListNode(curr2.val)
                curr2 = curr2.next
                currans = currans.next

        if curr1 :
            currans.next = curr1
        if curr2 :
            currans.next = curr2 

        return ans.next

        