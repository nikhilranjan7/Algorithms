class Solution:
    def isValid(self, s: str) -> bool:

        par_map = {'(':')', '[':']', '{':'}'}

        stack = []


        for i in s:
            if i in par_map.keys():
                stack.append(par_map[i])
            else:
                if len(stack) == 0:
                    return False

                symbol = stack.pop()
                if symbol != i:
                    return False

        if len(stack) != 0:
            return False

        return True

'''
Time complexity: O(N) - N is characters in string
Space complexity: O(N)
'''

'''
Improve points:
- 
'''
