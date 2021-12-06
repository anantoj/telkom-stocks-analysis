import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

file = 'Telkom Indonesia (Persero) Tbk. (TLKM.JK) Stock Historical Prices & Data - Yahoo Finance.html'

with open(file, 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

table = doc.find_all('tr', class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")

data=[]
headers = ['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']

# for header in headers:
#     data.append((header, []))


for i in range(len(table)):
    row = table[i].contents
    if len(row) != 7:
        continue
    row_mod = []
    for j in range(len(row)):
        if row[j].span == None:
            row_mod.append(np.NaN)
            continue
        row_mod.append(row[j].span.string)
    
    data.append(row_mod)




df=pd.DataFrame(data, columns=headers)
print(df.head())
print(df.shape)
df.to_csv('../telkom_stock_data.csv',index=False)







