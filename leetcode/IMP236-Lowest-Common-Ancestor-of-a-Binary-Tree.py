# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(node, parents_list=[]):
            nonlocal parents

            if node:
                if node.val == p.val:
                    parents['p'] = list(parents_list+[node.val])[::-1]

                if node.val == q.val:
                    parents['q'] = list(parents_list+[node.val])[::-1]

                traverse(node.left, parents_list+[node.val])
                traverse(node.right, parents_list+[node.val])

        parents = {}
        traverse(root)

        print(parents)

        i, j = 0, 0

        ans = 0

        while(True):
            if parents['p'][i] == parents['q'][j]:
                ans = parents['p'][i]
                break

            if len(parents['p'])-i < len(parents['q'])-j:
                j += 1

            elif len(parents['p'])-i > len(parents['q'])-j:
                i += 1

            else:
                i, j = i+1, j+1

        return TreeNode(ans)

'''
Time complexity: O(N) - N is number of nodes in Tree
Space complexity: O(N)
'''

'''
Improve points:
- Solve withing dfs function itself
'''
