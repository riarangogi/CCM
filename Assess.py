"""
Author: Ricardo Arango Giraldo
Date: 11/Mar/2019
Description: In  this script we select the classifiers of customers models
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.6.8
"""

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score

y_tree_pred=tree_gini.predict(X_test_tree)
acc_tree=accuracy_score(y_tree_test,y_tree_pred)
mat_tree=confusion_matrix(y_tree_test,y_tree_pred)
rep_tree=classification_report(y_tree_test,y_tree_pred)
acc_tree
mat_tree
rep_tree

y_os_tree_pred=os_tree_gini.predict(X_test_tree)
acc_os_tree=accuracy_score(y_tree_test,y_os_tree_pred)
mat_os_tree=confusion_matrix(y_tree_test,y_os_tree_pred)
rep_os_tree=classification_report(y_tree_test,y_os_tree_pred)
acc_os_tree
mat_os_tree
rep_os_tree

y_osre_tree_pred=osre_tree_gini.predict(X_test_tree)
acc_osre_tree=accuracy_score(y_tree_test,y_osre_tree_pred)
mat_osre_tree=confusion_matrix(y_tree_test,y_osre_tree_pred)
rep_osre_tree=classification_report(y_tree_test,y_osre_tree_pred)
acc_osre_tree
mat_osre_tree
rep_osre_tree