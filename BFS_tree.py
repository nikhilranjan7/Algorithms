# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

a = [[]]
def bfs(a, root):
  if root == None:
    return
  level = 0
  previous_level = 0
  q = deque([(root, level)])
  
  while(len(q) > 0):
    node = q.popleft()
    
    if node[1] != previous_level:
      previous_level += 1
      a.append([])
    
    a.append[previous_level](node[0].val)
    
    if node[0].left != None:
      q.apppend((node[0].left, node[1]+1))
    if node[0].right != None:
      q.apppend((node[0].right, node[1]+1))
  
  
