# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def traverse(node):
            if node != None:
                traverse(node.left)
                l.append(node.val)
                traverse(node.right)

        l = []
        traverse(root)

        return l


'''
Time complexity: O(N) - N is number of nodes in tree starting from root
Space complexity: O(N)
'''

'''
Improve points:
- Learn about space complexity of DFS/BFS
- Implement DFS iteratively
'''
