import pandas as pd 

#from subprocess import call
#call(["python", "Stock_reporter_no_panda.py"])

portfolio = pd.read_csv("portfolio_new.csv")
print(portfolio)

divide_columns = portfolio['Current price'] / portfolio['Purchase price'] - 1

percent_list = []
for i in divide_columns:
    number = i*100
    format_number = "{:.2f}".format(number)
    percent = (format_number + " %") 
    percent_list.append(percent)

print(percent_list)

portfolio["Percent"] = percent_list
portfolio.to_csv("Stock_list_final.csv", index=False)

portfolio.to_excel ("Stock_final.xlsx", index = None, header=True)
