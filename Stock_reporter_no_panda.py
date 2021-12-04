import yfinance as yf 
import csv

output = [] #contains only ticker and purchase price

#create new output just with desired rows
with open("Portfolio_test.csv", "r+") as stocks: 
    for line in stocks:
        cells = line.split(",")
        list(cells)
        output.append((cells[0], cells[10]))

print(output)

ticker = [] #contains only tickers

#append ticker with tickers only
for item in output[1:]:
    ticker.append(item[0])

    #loop over a list of stocks and return current price of each stock

print(ticker)    

purchase_price = []

for item in output[1:]:
    purchase_price.append(item[1])

current_price = []

for i in range(len(ticker)):
        
    price = str(ticker[i]) + "," + str(yf.Ticker(ticker[i]).info['regularMarketPrice'])
    tickers = price.split(",")
    list(tickers)

    current_price.append(tickers[1])

print(current_price)

header = ["Symbol", "Purchase price", "Current price"]

with open("portfolio_new.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(i for i in header)
    for row in zip(ticker, purchase_price, current_price):
            writer.writerow(row)









