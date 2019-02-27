import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data=pd.read_csv("./Data Raw/bigml_59c28831336c6604c800002a.csv")
data.head()

churn=data["churn"].value_counts()
state=data["state"].value_counts()
