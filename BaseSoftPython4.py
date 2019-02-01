'''
Each day we get a list of yesterdays stock prices, a list where:
The indices are the minutes since opening time
The values are the prices in dollars of the stock at that time.
So if the stock price was $250 after half an hour after opening:
yesterdays_stock_prices[30] = 250.
Your function should efficiently return the best profit we could have made from 1 purchase to 1
sale of stock, yesterday.
For example:
yesterdays_stock_prices = [8, 12, 4, 5, 7, 11, 10]
get_max(yesterdays_stock_prices)
# returns 7 (purchase at $4, sell at $11
Note that you cannot sell before you make a purchase and you cannot buy and sell at
the same time step
'''
import random

def get_stocksList():
    stockList = []
    # creates a 50 integer list with random integers
    for stock in range(50):
        stockList.append(random.randint(0, 100))
    print(stockList)
    return stockList


def get_max(stockList):
  profit = 0
  buy = stockList[0]

  for stock in range(1, len(stockList)):
    buy = min(buy, stockList[stock])
    profit = max(profit, stockList[stock] - buy)

  return profit


maxRetrieved = get_max(get_stocksList())
print(maxRetrieved)
