"""
Author: Ricardo Arango Giraldo
Date: 04/Mar/2019
Description: In  this script we built and developed the classifiers of customers
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.6.8
"""

from  sklearn.metrics import accuracy_score
from sklearn import tree
import graphviz as grp
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

tree_gini=tree.DecisionTreeClassifier(criterion="gini",random_state=47,max_depth=3,min_samples_leaf=5)
tree_gini=tree_gini.fit(X_train_tree,y_train_tree)
os_tree_gini=tree_gini.fit(os_X_train_tree,os_y_train_tree)
osre_tree_gini=tree_gini.fit(osre_X_train_tree,osre_y_train_tree)

dot=tree.export_graphviz(tree_gini,out_file=None,feature_names=columns,class_names=["No","Si"])
graph=grp.Source(dot)
graph.render("Tree")
os_dot=tree.export_graphviz(os_tree_gini,out_file=None,feature_names=columns,class_names=["No","Si"])
os_graph=grp.Source(os_dot)
os_graph.render("os_Tree")
osre_dot=tree.export_graphviz(osre_tree_gini,out_file=None,feature_names=columns,class_names=["No","Si"])
osre_graph=grp.Source(osre_dot)
osre_graph.render("osre_Tree")

log=sm.Logit(y_train,X_train_log)
result=log.fit()
result.summary2()