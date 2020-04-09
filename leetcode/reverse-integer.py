class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        u = []

        is_neg = 1
        if s[0] == '-':
            is_neg = -1
            s = s[1:]

        ans = 0
        for i in range(len(s)-1, -1, -1):
            ans = ans*10 + int(s[i])


        ans = ans*is_neg if -2**31 <= ans*is_neg <= 2**31 -1 else 0

        return ans

'''
Time complexity: O(log(x)) - base of log is 10 as number if digits in a number x is around log10 x
Space complexity: O(log(x))
'''

'''
Improve points:
-
'''
