import os
import yfinance as yf 
import csv

output = []

#create new output just with desired rows
with open("Portfolio.csv", "r+") as stocks: 
    for line in stocks:
        cells = line.split(",")
        output.append(( cells[ 0 ], cells[ 10]))


ticker = []

for item in output:
    ticker.append(item[0])




