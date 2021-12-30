import yfinance as yf #import Yahoo finance module
import csv #import csv module

output = [] #contains only ticker and purchase price

#create new output just with desired rows
with open("Portfolio.csv", "r+") as stocks: 
    for line in stocks:
        cells = line.split(",")
        list(cells)
        output.append((cells[0], cells[10], cells[11]))

print(output) #control

#contains only tickers from csv files
ticker = [] 

#append ticker with tickers only, avoids first row [0]
#loop over a list of stocks
for item in output[1:]:
    ticker.append(item[0])
    
print(ticker) #control

#contains quantity 
quantity = []

#append list with purchase price only, avoids first row [0]
#loop over a list of quantity
for item in output[2:]:
    quantity.append(item[2])

print(quantity)

#contains only purchase price
purchase_price = []

#append list with purchase price only, avoids first row [0]
#loop over a list of purchase price
for item in output[1:]:
    purchase_price.append(item[1])

#contains current market price
current_price = []

#takes list of tickers and adds current market price 
for i in range(len(ticker)):
        
    price = str(ticker[i]) + "," + str(yf.Ticker(ticker[i]).info['regularMarketPrice'])
    tickers = price.split(",")
    list(tickers)

    current_price.append(tickers[1])

print(current_price) #control

#header for csv file
header = ["Symbol", "Purchase price", "Current price", "Quantity"]

#writes to csv file ticker, purchase price, current market price
with open("portfolio_new.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(i for i in header)
    for row in zip(ticker, purchase_price, current_price, quantity):
            writer.writerow(row)

#final list for internal use
#final_list = []

#appends one list with multiple lists zip(), 
#for (a, b, c) in zip(ticker, purchase_price, current_price):
    #final_list.append(a)
    #final_list.append(b)
    #final_list.append(a)

#print(final_list) #control








