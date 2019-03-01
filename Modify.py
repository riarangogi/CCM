"""
Author: Ricardo Arango Giraldo
"""
import pandas as pd

data=pd.read_csv("./Data Tidy/bigml_tidy.csv")
data.head()

table=pd.crosstab(index=data["state"],columns=data["churn"])
df_table=pd.DataFrame(table)
df_table.head()

df_table["total customer"]=df_table[False]+df_table[True]
df_table["prop customer"]=df_table[True]/df_table["total customer"]
df_table.sort_values(by="prop customer",inplace=True)

states=df_table.index
state_dic={'state' : {state: i for state,i in zip(states,range(len(states)))}}

data.replace(state_dic,inplace=True)
data.head()

data["churn"]=data["churn"].astype(int)
international_dic={"international plan":{"no":0,"yes":1}}
data.replace(international_dic,inplace=True)
mail_dic={"voice mail plan":{"no":0,"yes":1}}
data.replace(mail_dic,inplace=True)
data.dtypes

y=data["churn"]
X=data.drop("churn",axis=1)