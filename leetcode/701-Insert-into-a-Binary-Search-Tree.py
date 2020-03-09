# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def travel(node, val):
            if node.val > val:
                if node.left == None:
                    node.left = TreeNode(val)
                else:
                    travel(node.left, val)

            elif node.val < val:
                if node.right == None:
                    node.right = TreeNode(val)
                else:
                    travel(node.right, val)

        if root == None:
            return TreeNode(val)

        travel(root, val)

        return root

'''
Time complexity: O(N) - N is number of nodes
Space complexity: O(N) - As corresponding to each nodes one function is stored in stack
'''

'''
Improve points:
- 
'''
