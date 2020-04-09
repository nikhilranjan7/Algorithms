from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)

        if len(count_s) != len(count_t):
            return False

        for i in count_s:
            if i not in count_t:
                return False
            else:
                if count_s[i] != count_t[i]:
                    return False

        return True

'''
Time complexity: O(N) - N is max of number of elements in s and t
Space complexity: O(N)
'''

'''
Improve points:
-
'''
