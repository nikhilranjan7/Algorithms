class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mode = 'buy'
        profit = 0

        for i in range(1, len(prices)):
            if mode == 'buy':
                if prices[i-1] < prices[i]:
                    profit -= prices[i-1]
                    mode = 'sell'

            else:
                if prices[i-1] > prices[i]:
                    profit += prices[i-1]
                    mode = 'buy'

        # for last element:
        if mode == 'sell':
            profit += prices[i]

        return profit

'''
Time complexity: O(N) - N is number of elements in prices
Space complexity: O(1)
'''

'''
Improve points:
-
'''
