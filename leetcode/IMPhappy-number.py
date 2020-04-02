class Solution:
    def isHappy(self, n: int) -> bool:

        already = set()

        while(True):
            s_n = str(n)
            digit_sum = 0
            for i in s_n:
                digit_sum += int(i)*int(i)

            if digit_sum == 1:
                return True
            elif digit_sum in already:
                return False

            n = digit_sum
            already.add(digit_sum)

'''
Time complexity:
Space complexity:
'''

'''
Improve points:
- Find timecomplexity for finding a prime
'''
