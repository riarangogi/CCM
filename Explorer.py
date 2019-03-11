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
plt.title("Total desercion en clientes")
plt.ylabel("Clientes")
plt.savefig("count_churn")
ratio_churn=()

table=pd.crosstab(index=data["state"],columns=data["churn"])
table.plot(kind="bar")
plt.title("Total desercion por estados")
plt.ylabel("Clientes")
plt.xlabel("Estados")
plt.savefig("count_churn_state")

table=pd.crosstab(index=data["international plan"],columns=data["churn"])
table.plot(kind="bar",stacked=True)
plt.title("Proporcion desercion en plan internacional")
plt.ylabel("Clientes")
plt.savefig("prop_churn_inrternational")

table=pd.crosstab(index=data["voice mail plan"],columns=data["churn"])
table.plot(kind="bar",stacked=True)
plt.title("Proporcion desercion en plan voz y datos")
plt.ylabel("Clientes")
plt.savefig("prop_churn_voice_mail")

plt.hist(data["account length"])
plt.title("Distribucion tamanos de cuentas")
plt.xlabel("Tamano de cuenta")
plt.savefig("hist_account_length")

plt.hist(data["number vmail messages"])
plt.title("Distribucion numero de mensajes enviados")
plt.xlabel("Cantidad de mensajes enviados")
plt.savefig("hist_number_messages")

fig,axs=plt.subplots(1,3)
fig.suptitle("Distribuciones comportamiento por el dia")
axs[0].hist(data["total day minutes"])
axs[0].set_xlabel("Minutos")
axs[1].hist(data["total day charge"])
axs[1].set_xlabel("Recargas")
axs[2].hist(data["total day calls"])
axs[2].set_xlabel( "Llamadas")
fig.savefig("cha_day")

fig,axs=plt.subplots(1,3)
fig.suptitle("Distribuciones comportamiento por la tarde")
axs[0].hist(data["total eve minutes"])
axs[0].set_xlabel("Minutos")
axs[1].hist(data["total eve charge"])
axs[1].set_xlabel("Recargas")
axs[2].hist(data["total eve calls"])
axs[2].set_xlabel( "Llamadas")
fig.savefig("cha_eve")

fig,axs=plt.subplots(1,3)
fig.suptitle("Distribuciones comportamiento por la noche")
axs[0].hist(data["total night minutes"])
axs[0].set_xlabel("Minutos")
axs[1].hist(data["total night charge"])
axs[1].set_xlabel("Recargas")
axs[2].hist(data["total night calls"])
axs[2].set_xlabel( "Llamadas")
fig.savefig("cha_night")

data["total intl minutes"].hist()

data["total intl charge"].hist()

data["total intl calls"].hist()

plt.hist(data["customer service calls"])
plt.title("Distribucion numero de llamadas servicio al cliente")
plt.xlabel("Cantidad de llamadas")
plt.savefig("hist_customer_calls")

data.drop(["phone number","area code"],axis=1,inplace=True)
data.head()

os.mkdir("./Data Tidy")
data.to_csv("./Data Tidy/bigml_tidy.csv",index=False)