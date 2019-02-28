import pandas as pd

data=pd.read_csv("./Data Raw/bigml_59c28831336c6604c800002a.csv")
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