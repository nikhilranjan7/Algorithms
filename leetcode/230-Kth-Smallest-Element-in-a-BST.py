# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def traverse(node):
            nonlocal found, ans, count

            if node and not found:
                traverse(node.left)
                if count == k:
                    found = True
                    ans = node.val
                count += 1
                traverse(node.right)


        found = False
        ans = -1
        count = 1

        traverse(root)

        return ans

'''
Time complexity: O(N) - N is number of nodes in TreeNode root
Space complexity: O(N)
'''

'''
Improve points:
-
'''
