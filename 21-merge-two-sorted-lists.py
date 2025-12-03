from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 5 -> 7
        # 1 -> 3 -> 4 -> 6
        # 1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        # Approach: Compare head1 and head2, make the smaller root of new list
        # change head1/head2 whichever smaller to the next node and compare until one list is empty, then add the entirety of the next list
        newList = ListNode()
        head = newList
        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1

        while (list1 != None or list2 != None):
            if (list1.val < list2.val):
                newList.val = list1.val
                list1 = list1.next
                if (list1 == None):
                    newList.next = list2
                    break
            else:
                newList.val = list2.val
                list2 = list2.next
                if (list2 == None):
                    newList.next = list1
                    break
            newList.next = ListNode()
            newList = newList.next
        
        return head

# Helper methods to test the code
def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(head):
    cur = head
    result = []
    while cur:
        result.append(cur.val)
        cur = cur.next
    print(result)

list1 = build_list([1, 2, 3])
list2 = build_list([1, 2, 4])
s = Solution()
new_head = s.mergeTwoLists(list1, list2)
print_list(new_head)