buy, sell, max_profit = 0, 1, 0
prices = [7,1,5,3,6,4]
while sell < len(prices):
    if prices[buy] < prices[sell]:
        profit = prices[sell] - prices[buy]
        max_profit = max(max_profit, profit)
    else:
        buy = sell
    sell += 1
print (max_profit)