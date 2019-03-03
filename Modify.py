"""
Author: Ricardo Arango Giraldo
Date: 28/Feb/2019
Description: In  this script we make all process about modify the dataset for  modeling and analysis
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.6.8
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

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
seed=np.random.seed(47)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=seed)

os=SMOTE(random_state=seed)
os_X_train, os_y_train=os.fit_resample(X_train,y_train)