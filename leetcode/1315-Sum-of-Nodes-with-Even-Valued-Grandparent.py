# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def traverse(node, parent=None, grandparent=None):
            nonlocal ans

            if node:

                if parent and grandparent and grandparent.val%2 == 0:
                    ans += node.val
                traverse(node.left, node, parent)
                traverse(node.right, node, parent)


        ans = 0

        traverse(root)

        return ans

'''
Time complexity: O(N) - N is number of nodes in Tree
Space complexity: O(N) - In worst case, N function calls if all the nodes have only one children
'''

'''
Improve points:
-
'''
