from typing import Optional
from typing import List

def insertNode(root: TreeNode, newVal: int):
    if (root.val > newVal):
        if (root.left):
            return insertNode(root.left, newVal)
        else:
            root.left = TreeNode(newVal)
    else:
        if (root.right):
            return insertNode(root.right, newVal)
        else: 
            root.right = TreeNode(newVal)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Approach: 
        # 1. Create Root node from 0th index of list
        # 2. Go left and create .left nodes until left leaf of tree
        # 3. Go up 1 and then go right
        # 4. Go left until leaf
        # Continue the loop of step 3 and 4
        if (len(preorder) == 0):
            return
        
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            insertNode(root, preorder[i])
        return root


s = Solution()
head = s.bstFromPreorder([8,4,1,5,6,11,9,10,15,13,12,17])