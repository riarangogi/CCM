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
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
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
np.random.seed(47)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=47)
columns=X_train.columns
dic_targets={0:"No",1:"Si"}
os=SMOTE(random_state=47)

os_X_train, os_y_train=os.fit_sample(X_train,y_train)
os_X_train=pd.DataFrame(data=os_X_train,columns=columns)
os_y_train=pd.DataFrame(data=os_y_train,columns=["y"])
len(X_train), len(os_X_train)
len(os_y_train[os_y_train["y"]==0]), len(os_y_train[os_y_train["y"]==1])

osre_X_train, osre_y_train=os.fit_sample(X_train,y_train)
osre_X_train=pd.DataFrame(data=osre_X_train,columns=columns)
osre_y_train=pd.DataFrame(data=osre_y_train,columns=["y"])
len(X_train), len(osre_X_train)
len(osre_y_train[osre_y_train["y"]==0]), len(osre_y_train[osre_y_train["y"]==1])

X_train_tree=X_train.copy()
y_train_tree=y_train.copy()
y_train_tree.replace(dic_targets,inplace=True)
y_train_tree=y_train_tree.values
X_train_tree["state"]=X_train_tree["state"].astype("category")
os_X_train_tree=os_X_train.copy()
os_y_train_tree=os_y_train["y"].copy()
os_y_train_tree.replace(dic_targets,inplace=True)
os_y_train_tree=os_y_train_tree.values
os_X_train_tree["state"]=os_X_train_tree["state"].astype("category")
osre_X_train_tree=osre_X_train.copy()
osre_y_train_tree=osre_y_train["y"].copy()
osre_y_train_tree.replace(dic_targets,inplace=True)
osre_y_train_tree=osre_y_train_tree.values
osre_X_train_tree["state"]=osre_X_train_tree["state"].astype("category")

logreg=LogisticRegression(random_state=47)
rfe=RFE(logreg,11)

rfe=rfe.fit(X_train,y_train.values)
sup=rfe.support_
X_train_log=X_train.iloc[:,sup]

os_y_train_log=os_y_train["y"].copy()
os_y_train_log=os_y_train_log.values
os_rfe=rfe.fit(os_X_train,os_y_train_log)
os_sup=os_rfe.support_
os_X_train_log=os_X_train.iloc[:os_sup]

osre_X_train_log=osre_X_train.copy()
osre_y_train_log=osre_y_train["y"].copy()
osre_y_train_log=osre_y_train_log.values