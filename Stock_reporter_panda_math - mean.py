import pandas as pd 

#from subprocess import call
#call(["python", "Stock_reporter_no_panda.py"])

portfolio = pd.read_csv("portfolio_new.csv")
#portfolio.set_index(['Symbol', 'Purchase price', 'Current price']).groupby(level=['Symbol', 'Purchase price', 'Current price']).mean()
df = portfolio.groupby(['Symbol'], as_index= False).mean()
print(df)

divide_columns = df['Current price'] / df['Purchase price'] - 1

percent_list = []
for i in divide_columns:
    number = i*100
    format_number = "{:.2f}".format(number)
    percent = (format_number + " %") 
    percent_list.append(percent)

print(percent_list)

df["Percent"] = percent_list
df.to_csv("Stock_list_final.csv", index = False)

df.to_excel ("Stock_final.xlsx", index = None, header=True)

