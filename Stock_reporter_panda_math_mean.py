#!/usr/local/bin/python3
import pandas as pd 

#from subprocess import call
#call(["python", "Stock_reporter_no_panda.py"])

#read cdv from stock_reporter module
portfolio_read = pd.read_csv("portfolio_new.csv")

#check for duplicates and make meand, avoin indexes
portfolio = portfolio_read.groupby(['Symbol'], as_index= False).mean()
print(portfolio) #control

#make gain/lose in %
divide_columns = portfolio['Current price'] / portfolio['Purchase price'] - 1

#create new list with %
percent_list = []
for i in divide_columns:
    number = i*100
    format_number = "{:.2f}".format(number)
    percent = (format_number + " %") 
    percent_list.append(percent)

print(percent_list)

#write total gain % to csv/excel
portfolio["Total gain (%)"] = percent_list
portfolio.to_csv("Stock_list_final.csv", index = False)

#portfolio.to_excel("Stock_final.xlsx", index = None, header=True)

