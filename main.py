import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("./Data Raw/bigml_59c28831336c6604c800002a.csv")
data.dtypes
data.isnull().sum()
data.head()

data["churn"].hist()

table=pd.crosstab(index=data["state"],columns=data["churn"])
table.plot(kind="bar")

table=pd.crosstab(index=data["international plan"],columns=data["churn"])
table.plot(kind="bar",stacked=True)

table=pd.crosstab(index=data["voice mail plan"],columns=data["churn"])
table.plot(kind="bar",stacked=True)

data["account length"].hist()

data["number vmail messages"].hist()

data["total day minutes"].hist()

data["total day charge"].hist()

data["total day calls"].hist()

data["total eve minutes"].hist()

data["total eve charge"].hist()

data["total eve calls"].hist()

data["total night minutes"].hist()

data["total night charge"].hist()

data["total night calls"].hist()

data["total intl minutes"].hist()

data["total intl charge"].hist()

data["total intl calls"].hist()

data["customer service calls"].hist()

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

data.drop(["phone number","area code"],axis=1,inplace=True)
data.head()

y=data["churn"]
X=data.drop("churn",axis=1)

ratio_churn=()