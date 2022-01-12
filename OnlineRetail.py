#%%
import pandas as pd
import numpy as np
df= pd.read_csv("OnlineRetail.csv")
df

# %%
table_Country = pd.pivot_table(df, values='Quantity', index=['Country'],
                    columns=['InvoiceNo'], aggfunc=np.sum)
table_Country

# %%
table_CustomerID = pd.pivot_table(df, values='Quantity', index=['StockCode','CustomerID'],
                    aggfunc={'Quantity': [min,max]})
table_CustomerID

# %%
table_StockCode = pd.pivot_table(df, values=['Quantity', 'UnitPrice'], index=['Country'],
                    aggfunc={'Quantity': np.sum,
                             'UnitPrice': np.mean})
table_StockCode

# %%
table_InvoiceDate = pd.pivot_table(df, values='Quantity', index=['InvoiceDate','Country'],
                    aggfunc=np.sum)
table_InvoiceDate

# %%
