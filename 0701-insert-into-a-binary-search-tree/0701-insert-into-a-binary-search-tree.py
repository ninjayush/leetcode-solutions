# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)
        head=root
        parent=root
        while head:
            parent=head
            if val<head.val:
                head=head.left
            else:
                head=head.right
        
        peel=TreeNode(val)
        if val<parent.val:
            parent.left=peel
        else:
            parent.right=peel
        
        return root