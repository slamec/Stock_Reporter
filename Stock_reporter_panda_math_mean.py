#!/usr/local/bin/python3
import pandas as pd 

#read cdv from stock_reporter module
portfolio_read = pd.read_csv("portfolio_new.csv")

#check for duplicates and make meand, avoin indexes
portfolio = portfolio_read.groupby(['Symbol'], as_index= False).mean()
print(portfolio) #control

#sum of tickers quantity 
portfolio_sum = portfolio_read.groupby(['Symbol'], as_index= False).sum()

#used for quantity as number
total_quantity = portfolio_sum['Quantity']
#make gain/lose in %
divide_columns = (total_quantity * portfolio['Current price']) / (total_quantity * portfolio['Purchase price']) - 1
#count differences
difference = portfolio['Current price'] - portfolio['Purchase price']
#total absolute gain 
total_gain = (total_quantity * portfolio['Current price']) - (total_quantity * portfolio['Purchase price'])


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
for i in total_quantity:
    quantity_format = "{:2f}".format(i)
    quantity_list.append(quantity_format)

#new list of total absolute gain
total_gain_list = []
for i in total_gain:
    gain_format = "{:.2f}".format(i)
    total_gain_list.append(gain_format)


#delete original 'Quantity' column
del portfolio['Quantity']

#convert list to floating numbers 
portfolio_sum_int = [int(float(i)) for i in total_gain_list]

#sum of positive and negative numbers from the list
portfolio_sum_positive = [i for i in portfolio_sum_int if i >= 0]
portfolio_sum_negative = [i for i in portfolio_sum_int if i < 0]
portfolio_total_gain = (sum(portfolio_sum_positive) / sum(portfolio_sum_negative) - 1) * (-1) 

#make new rows to a csv/excel
portfolio["Quantity"] = quantity_list
portfolio["Current Difference"] = difference_list
portfolio["Total gain"] = total_gain_list
portfolio["Total gain (%)"] = percent_list
portfolio["P/L (%)"] = "{:.2f} {}".format(portfolio_total_gain, "%")

#write everything to a CSV and Excel
portfolio.to_csv("Stock_list_final.csv", index = False)
portfolio.to_excel("Stock_final.xlsx", index = None, header=True)


