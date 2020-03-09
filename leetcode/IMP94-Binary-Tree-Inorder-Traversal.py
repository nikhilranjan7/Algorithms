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
    - Space complexity of iterative and recursive implementation is same. Depends on size of queue i.e. dependent on size of nodes O(N)
- Implement DFS iteratively

    def traverse_preorder(node):
        stack = []
        level = 0
        stack.append((node, level))
        preorder = []
        while(len(stack) != 0):
            n, level = stack.pop()
            if n != None:
                preorder.append((n.val, level))
            stack.append((n.right, level+1))
            stack.append((n.left, level+1))

'''
