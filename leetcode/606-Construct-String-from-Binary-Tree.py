# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:

        def dfs(node):
            nonlocal ans
            if node != None:
                ans += '('
                ans += str(node.val)

                if node.left == None and node.right != None:
                    ans += '()'
                dfs(node.left)
                dfs(node.right)
                ans += ')'

        ans = ''
        dfs(t)

        return ans[1:-1]


'''
Time complexity: O(N) - N is number of nodes in TreeNode t
Space complexity: O(N)
'''

'''
Improve points:
-
'''
