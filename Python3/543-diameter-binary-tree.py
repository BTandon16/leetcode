# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return 0

s = Solution()
root = TreeNode(8, 
                left = TreeNode(4, left = TreeNode(1), right = TreeNode(6)),
                right = TreeNode(14, left = TreeNode(12, left = TreeNode(11, left = TreeNode(10, left = TreeNode(9)))), 
                                 right = TreeNode(18, left = TreeNode(15, right = TreeNode(16)), 
                                                  right = TreeNode(23, left = TreeNode(20), right = TreeNode(27, left = TreeNode(25, left = TreeNode(24))))
                                                )
                                )
                )
print(s.diameterOfBinaryTree(root))