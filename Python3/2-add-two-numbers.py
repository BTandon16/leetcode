# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Could be faster for solution, uses intricacies from Python so could have more appropriate logic too
        num1 = ''
        num2 = ''

        while (l1 is not None or l2 is not None):
            if (l1 is not None):
                num1 = str(l1.val) + num1
                l1 = l1.next
            if (l2 is not None):
                num2 = str(l2.val) + num2
                l2 = l2.next
        final = int(num1) + int(num2)
        final = str(final)
        l3 = ListNode()
        node = l3
        for i in range(len(final) - 1, -1, -1):
            node.val = int(final[i])
            if (i != 0):
                node.next = ListNode()
                node = node.next
        return l3

