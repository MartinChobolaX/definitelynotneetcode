def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    l,r = 0,1
    maxProfit = 0
    while r < len(prices):
        cur_profit = prices[r] - prices[l]
        if prices[l] > prices[r]:
            l = r
        else:
            maxProfit = max(maxProfit, cur_profit)
        r += 1
    return maxProfit

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
result1 = maxProfit(prices1)
result2 = maxProfit(prices2)
print(result1)
print(result2)