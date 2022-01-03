#!/usr/local/bin/python3
import pandas as pd 

#from subprocess import call
#call(["python", "Stock_reporter_no_panda.py"])

#read cdv from stock_reporter module
portfolio_read = pd.read_csv("portfolio_new.csv")

#check for duplicates and make meand, avoin indexes
portfolio = portfolio_read.groupby(['Symbol'], as_index= False).mean()
print(portfolio) #control

#sum of tickers quantity 
portfolio_sum = portfolio_read.groupby(['Symbol'], as_index= False).sum()

#used for quantity as number
sum = portfolio_sum['Quantity']
#make gain/lose in %
divide_columns = (sum * portfolio['Current price']) / (sum * portfolio['Purchase price']) - 1
#count differences
difference = portfolio['Current price'] - portfolio['Purchase price']
#total absolute gain 
total_gain = (sum * portfolio['Current price']) - (sum * portfolio['Purchase price'])


#create new list with %
percent_list = []
for i in divide_columns:
    number = i*100
    format_number = "{:.2f}".format(number)
    percent = (format_number + " %") 
    percent_list.append(percent)

#create a list with differences
difference_list = []
for i in difference:
    diff_format = "{:.2f}".format(i)
    difference_list.append(diff_format)

#cerate new quantity list
quantity_list = []
for i in sum:
    quantity_format = "{:2f}".format(i)
    quantity_list.append(quantity_format)

#new list of total absolute gain
total_gain_list = []
for i in total_gain:
    gain_format = "{:.2f}".format(i)
    total_gain_list.append(gain_format)

print(percent_list)
print(difference_list)
print(quantity_list)

#delete original 'Quantity' column
del portfolio['Quantity']

#write total gain % to csv/excel
portfolio["Quantity"] = quantity_list
portfolio["Current Difference"] = difference_list
portfolio["Total gain"] = total_gain_list
portfolio["Total gain (%)"] = percent_list
portfolio.to_csv("Stock_list_final.csv", index = False)

portfolio.to_excel("Stock_final.xlsx", index = None, header=True)


