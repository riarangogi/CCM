import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

data=pd.read_csv("./Data Raw/bigml_59c28831336c6604c800002a.csv")
data.head()

table=pd.crosstab(data["state"],data["churn"])
df_table=pd.DataFrame(table)

df_table["total customer"]=df_table[False]+df_table[True]
df_table["prop customer"]=df_table[True]/df_table["total customer"]

df_table.sort_values(by="prop customer",inplace=True)
df_table["encoding"]=range(len(df_table))
df_table.head()


df_table=pd.DataFrame(table)
table_2["encoding"]=range(len(table_2))

state_dic={

}