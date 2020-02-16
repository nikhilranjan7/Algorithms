class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        start = len(digits) - 1
        while(True):
            if start == -1 and carry == 1:
                digits.insert(0,1)
                break

            number = (digits[start]+1)%10
            carry = (digits[start]+1)//10
            digits[start] = number
            start -= 1


            if carry == 0:
                 break

        return digits


'''
Time complexity: O(N) - N is number of elements in digits
Space complexity: O(1)
'''

'''
Improve points:
-
'''
