import os
import yfinance as yf 
import csv

output = [] #contains only ticker and purchase price

#create new output just with desired rows
with open("Portfolio.csv", "r+") as stocks: 
    for line in stocks:
        cells = line.split(",")
        output.append(( cells[ 0 ], cells[ 10]))


ticker = [] #contains only tickers

#append ticker with tickers only
for item in output:
    ticker.append(item[0])

def current_stock_price():
    #loop over a list of stocks and return current price of each stock
    i = 0
    
    while i < len(ticker):
        price = print(str(ticker[i]) + " " + str(yf.Ticker(ticker[i]).info['regularMarketPrice']))
        i += 1
    return i, price

current_prices = current_stock_price()
print(current_prices)



