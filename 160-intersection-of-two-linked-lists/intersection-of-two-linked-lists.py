# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = set()

        nodeA = headA

        while nodeA :
            if nodeA in d :
                pass
            else :
                d.add(nodeA) 
            nodeA = nodeA.next 
        
        nodeB = headB

        while nodeB :
            if nodeB in d :
                return nodeB
            nodeB = nodeB.next
        
        return None
        