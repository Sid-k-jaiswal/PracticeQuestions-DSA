class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [7,1,5,3,6,4] => p->7, max_profit = 0, min = 7
        #                  p->1, max = 0, min = 1
        #                  p->5, max = 4, min = 1
        #                  p->3, max = 4, min = 1
        #                  p->6, max = 5, min = 1
        #                  p->4, max = 5, min = 1



        min_price = 9999999
        max_profit = 0

        for p in prices:
            max_profit = max(max_profit, p - min_price)

            if p < min_price:
                min_price = p
        
        return max_profit