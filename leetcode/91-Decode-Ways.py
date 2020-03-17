class Solution:
    def numDecodings(self, s: str) -> int:


        if len(s) == 1:
            if 1 <= int(s[0]) <= 26:
                return 1
            else:
                return 0

        if len(s) == 0:
            return 0

        if s[0] == '0':
            return 0

        dp_table = [0]*(len(s)+1)

        #base-case
        dp_table[0] = 1
        dp_table[1] = 1

        #induction
        for i in range(2, len(s)+1):

            if 10 <= int(s[i-2] + s[i-1]) <= 26:
                dp_table[i] += dp_table[i-2]

            if 1 <= int(s[i-1]) <= 9:
                dp_table[i] += dp_table[i-1]


        return dp_table[-1]

'''
Time complexity: O(N) - N is number of letter in string s
Space complexity: O(N) # Can be converted to O(1) as only two elements need to be stored, not the whole table
'''

'''
Improve points:
-
'''
