from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def traverse(node):

            level_order = []

            queue = deque([(node, 0)])

            while(len(queue) > 0):
                curr_node, level = queue.popleft()

                if len(level_order) < level+1:
                    level_order.append([])

                if curr_node:
                    level_order[level].append(curr_node.val)

                    queue.append((curr_node.left, level+1))
                    queue.append((curr_node.right, level+1))

            return level_order[:-1]

        return traverse(root)

'''
Time complexity: O(N) - N is number of nodes in Tree
Space complexity: O(N) 
'''

'''
Improve points:
-
'''
