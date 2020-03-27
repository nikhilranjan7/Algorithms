class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        mul_val = 1
        if numerator < 0:
            mul_val *= -1
            numerator = abs(numerator)

        if denominator < 0:
            mul_val *= -1
            denominator = abs(denominator)

        prepend = '' if mul_val==1 else '-'

        q = numerator//denominator
        r = numerator%denominator

        ans = str(q) + '.'

        state = set()

        n, d = r, denominator
        is_repeat = False
        decimal_part = []
        while(True):
            n = n*10
            q = n//denominator
            r = n%denominator

            if r == 0:
                decimal_part.append(str(q)+'-'+str(r))
                break

            key = str(q)+'-'+str(r)

            if key in state:
                is_repeat = True
                decimal_part_processed = ''
                for i in decimal_part:
                    if key == i:
                        decimal_part_processed += '('
                    decimal_part_processed += i[0]
                decimal_part_processed += ')'
                break

            else:
                decimal_part.append(str(q)+'-'+str(r))
                state.add(key)

            n = r

        if is_repeat == False:
            decimal_part_processed = "".join([i[0] for i in decimal_part])

        if len(decimal_part_processed) == 1 and decimal_part_processed[0] == '0':
            return str(eval(prepend+ans[:-1]))

        return prepend+ans+decimal_part_processed

'''
Time complexity:
Space complexity:
'''

'''
Improve points:
- Find time and space complexity of this problem
'''
