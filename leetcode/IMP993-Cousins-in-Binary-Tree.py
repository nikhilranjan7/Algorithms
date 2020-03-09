# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def depthparent(node, n, depth=0, parent=-1):
            if node != None:
                if node.val == n:
                    ans.append((depth, parent))
                    return
                else:
                    depthparent(node.left, n, depth+1, node.val)
                    depthparent(node.right, n, depth+1, node.val)

            return depth, parent

        ans = []
        depthparent(root, x)
        depthparent(root, y)

        return (ans[0][0] == ans[1][0] and ans[0][1] != ans[1][1])

'''
Time complexity: O(N) - N is number of nodes
Space complexity: O(1)
'''

'''
Improve points:
- Carry variable value upwards in recursive functions without using list
- Solve same question using BFS approach
'''
