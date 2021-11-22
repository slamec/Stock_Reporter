import os
import yfinance as yf 
import csv

output = [] #contains only ticker and purchase price

#create new output just with desired rows
with open("Portfolio_test.csv", "r+") as stocks: 
    for line in stocks:
        cells = line.split(",")
        list(cells)
        output.append((cells[ 0 ], cells[ 10]))

print(output)

ticker = [] #contains only tickers

#append ticker with tickers only
for item in output:
    ticker.append(item[0])


def current_stock_price():
    #loop over a list of stocks and return current price of each stock
    
    current_price = []

    for i in range(len(ticker)):
        
        price = str(ticker[i]) + "," + str(yf.Ticker(ticker[i]).info['regularMarketPrice'])
        tickers = price.split(",")
        list(tickers)

        current_price.append((tickers[0], tickers[1]))

    current_price.append(output) #output should be splitted same as current price list
    return current_price

print(current_stock_price())

with open("portfolio_new.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(current_stock_price())




#connect output and ticker and write it to a file






