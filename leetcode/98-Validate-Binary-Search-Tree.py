# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def traverse(node, min_val=float('-inf'), max_val=float('+inf')):
            nonlocal ans

            if node and ans:
                if node.left and ( node.val <= node.left.val or not (min_val < node.left.val < max_val) ):
                    ans = False
                if node.right and ( node.val >= node.right.val or not (min_val < node.right.val < max_val) ):
                    ans = False

                traverse(node.left, min_val, node.val)
                traverse(node.right, node.val, max_val)

        ans = True
        traverse(root)

        return ans

'''
Time complexity: O(N) - N is number of nodes in Tree
Space complexity: O(N) - as max N-functions can be called on top of one another
'''

'''
Improve points:
-
'''
