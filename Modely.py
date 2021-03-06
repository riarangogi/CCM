"""
Author: Ricardo Arango Giraldo
Date: 04/Mar/2019
Description: In  this script we built and developed the classifiers of customers
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.6.8
"""

from sklearn import tree
import graphviz as grp
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

tree_d=tree.DecisionTreeClassifier(criterion="gini",random_state=47,
    max_depth=5,min_samples_split=20,min_samples_leaf=10)
tree_gini=tree_d.fit(X_train_tree,y_train_tree)
os_tree_gini=tree_d.fit(os_X_train_tree,os_y_train_tree)
osre_tree_gini=tree_d.fit(osre_X_train_tree,osre_y_train_tree)

dot=tree.export_graphviz(tree_gini,out_file=None,feature_names=columns,
    class_names=["No","Si"])
graph=grp.Source(dot)
graph.render("Tree")
os_dot=tree.export_graphviz(os_tree_gini,out_file=None,feature_names=columns,
    class_names=["No","Si"])
os_graph=grp.Source(os_dot)
os_graph.render("os_Tree")
osre_dot=tree.export_graphviz(osre_tree_gini,out_file=None,feature_names=columns,
    class_names=["No","Si"])
osre_graph=grp.Source(osre_dot)
osre_graph.render("osre_Tree")

log=sm.Logit(y_train.values,X_train_log)
result=log.fit()
result.summary2()

os_log=sm.Logit(os_y_train_log,os_X_train_log)
os_result=os_log.fit()
os_result.summary2()

osre_log=sm.Logit(osre_y_train_log,osre_X_train_log)
osre_result=osre_log.fit()
osre_result.summary2()