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

tree_gini=tree.DecisionTreeClassifier(criterion="gini",random_state=47,max_depth=3,min_samples_leaf=5)
tree_gini=tree_gini.fit(X_train_tree,y_train)

dot=tree.export_graphviz(tree_gini,out_file=None,feature_names=columns)
graph=grp.Source(dot)
graph.render("Tree")