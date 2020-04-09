class Solution:
    def isPalindrome(self, s: str) -> bool:

        u = []
        for i in s:
            if i.isalnum():
                u.append(i.lower())

        for i in range(len(u)//2):
            if u[i] != u[len(u)-1-i]:
                return False

        return True

'''
Time complexity: O(N) - N is number of elements in s
Space complexity: O(N)
'''

'''
Improve points:
-
'''
