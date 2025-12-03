from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5 -> null
        # Approach: (Brute Force) - Set a counter variable to count from 1 to N (N being the tail node)
        # Count till N - n times and remove that node (O(n^2))

        # Keep two nodes, 1 that checks next n times
        # After n times, set next to both nodes until you reach the end
        
        tail = head
        oneBeforeRemove = head
        counter = 0
        while (tail.next):
            if (counter == n):
                oneBeforeRemove = oneBeforeRemove.next
            else:
                counter += 1
            tail = tail.next

        # For empty linked lists after removal
        if (head == tail and n == 1):
            return None

        if (oneBeforeRemove.next):
            # In situations where the head has to be removed
            if (counter == n - 1):
                return oneBeforeRemove.next
            
            if (oneBeforeRemove.next.next):
                oneBeforeRemove.next = oneBeforeRemove.next.next
            else: 
                oneBeforeRemove.next = None

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

head = build_list([1, 2, 3])
s = Solution()
new_head = s.removeNthFromEnd(head, 3)
print_list(new_head)