# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp1 = l1
        temp2 = l2 
        ans_head = ListNode(-1)
        ans = ans_head
        carry = 0
        while temp1 and temp2 :
            sum = temp1.val + temp2.val + carry
            include = sum % 10
            carry = sum // 10 

            node = ListNode(include)
            print(node.val)
            ans.next = node
            ans = ans.next
            temp1 = temp1.next
            temp2 = temp2.next

        while temp1 :
            sum = temp1.val + carry
            include = sum % 10
            carry = sum // 10

            node = ListNode(include)
            print(node.val)
            ans.next = node
            ans = ans.next 
            temp1 = temp1.next

        while temp2 :
            sum = temp2.val + carry
            include = sum % 10
            carry = sum // 10

            node = ListNode(include)
            print(node.val)
            ans.next = node
            ans = ans.next
            temp2 = temp2.next
            
        if carry :
            node = ListNode(carry) 
            ans.next = node
        return ans_head.next