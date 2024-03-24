import pandas as pd
import json
import numpy as np

# office = pd.read_excel("SampleData.xlsx")
# office = office.dropna(how='all')
# df = office[office['Unnamed: 2'].str.contains("Sample")]

# abc = office[["Unnamed: 2", "Unnamed: 0"]]
# # Alist = range(20)
# df = pd.Series(Alist, index=[0,1,2,3,4,5])

json_data = json.loads(open(r"C:\Users\aditi\OneDrive\Documents\Python practice\other_file.json").read())
print(json_data)


cols = json_data["groups"][0]["columns"]
headers = json_data["headers"]
# df = pd.read_json("other_file.json")
# print(df.to_markdown())
df = pd.DataFrame(cols ,index=headers)
print(df)
df.loc["week"] = "changed_column"
# df = df.pivot_table(headers)
print(df)
# dates = pd.date_range("20130101", "20140101", periods=6)
'''KWid     Orders    Revenue
12345    10        150
23468    5         200'''
orders_1 = pd.DataFrame([['12345','10','150'],['23468','5','200']],columns=["KWid","Orders","Revenue"])
print(orders_1.to_markdown())

rows = []
new_table_columns = ["KWid","Orders","Revenue","OrderID"]
for k in orders_1["KWid"]:
    print(k)
    print( orders_1.loc[orders_1["KWid"]==k, 'Orders'].iloc[0])
    freq= int(orders_1.loc[orders_1["KWid"]==k, 'Orders'].iloc[0])
    cl1 = [k]*freq
    cl2 = [1]*freq
    cl3 = [int(orders_1.loc[orders_1["KWid"]==k, 'Revenue'].iloc[0])/freq]*freq
    cl4 = list(range(0,freq))

    new_table = pd.DataFrame([cl1,cl2,cl3,cl4], index=new_table_columns)
    new_table = new_table.T
    print(new_table.to_markdown())

print(new_table.stack())
print(pd.merge(orders_1, new_table, on="KWid"))
