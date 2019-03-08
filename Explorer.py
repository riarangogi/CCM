""""
Author: Ricardo Arango Giraldo
Date: 26/Feb/2019
Description: In  this script we explere the variabes that has the dataset
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.6.8
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

data=pd.read_csv("./Data Raw/bigml_59c28831336c6604c800002a.csv")
data.dtypes
data.isnull().sum()
data.head()

churn_txt=data["churn"].astype(object)
table=churn_txt.value_counts()
table.plot(kind="bar")
ratio_churn=()

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

data.drop(["phone number","area code"],axis=1,inplace=True)
data.head()

os.mkdir("./Data Tidy")
data.to_csv("./Data Tidy/bigml_tidy.csv",index=False)