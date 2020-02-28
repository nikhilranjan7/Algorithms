class Solution:
    def longestPalindrome(self, s: str) -> int:

        count_dict = {}

        for i in s:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        odd = 0
        ans = 0
        for i in count_dict.values():
            if i%2 != 0:
                odd = 1
                ans += i-1
            else:
                ans += i

        return ans + odd

'''
Time complexity: O(N) - N is number of letters in string s
Space complexity: O(N)
'''

'''
Improve points:
- Convert to O(1) as size of alphabet is finite
'''
