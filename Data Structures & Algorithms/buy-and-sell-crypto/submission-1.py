class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        highIndex = 0
        lowIndex = 0
        for i in range(len(prices)):
            if prices[i] < prices[lowIndex]:
                lowIndex = i
                highIndex = i
            if prices[i] > prices[highIndex]:
                highIndex = i
                profit = max(profit, prices[highIndex] - prices[lowIndex])

        return profit
            