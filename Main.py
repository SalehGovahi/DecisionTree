import pandas as pd
from Tree import *

train_feature_dataframe = pd.read_csv("./Data/feature_train-Copy.csv")
train_label_dataframe = pd.read_csv("./Data/label_train-Copy.csv")

tree = Tree()

print(f"Parent Entropy : {tree.calculate_parent_entropy(train_label_dataframe)}")
print("----------------------------------------------------------")
print("Features Entropy:")
filters_to_delete = []
print(tree.calculate_features_entropy(train_feature_dataframe,filters_to_delete))
print("----------------------------------------------------------")
print("Gain : ")
print(tree.calculate_gain(train_label_dataframe, tree.calculate_features_entropy(train_feature_dataframe)))
print("----------------------------------------------------------")
print(tree.find_max_gain(train_label_dataframe, tree.calculate_features_entropy(train_feature_dataframe)))
print("----------------------------------------------------------")
feature_name = tree.find_max_gain(train_label_dataframe, tree.calculate_features_entropy(train_feature_dataframe))
tree.create_child(train_feature_dataframe,train_label_dataframe,feature_name)
