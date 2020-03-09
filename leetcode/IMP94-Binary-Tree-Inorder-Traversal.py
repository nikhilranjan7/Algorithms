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

    def traverse_inorder(node):
        stack = []
        level = 0
        stack.append((node, level))
        inorder = []
        current = node.left
        while(True):

            if len(stack) > 0:
                if current != None:
                    stack.append((current.left, level+1))
                    current = current.left
                    level += 1
                    continue

                current, level = stack.pop()
                inorder.append((current.val, level))
                current, level = current.right, level+1

    def traverse_postorder(node):
        
'''
