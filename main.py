import pandas as pd
from Calculating import *
from Tree import *


feature_train_data = pd.read_csv("./Data/feature_train.csv").iloc[:]
label_train_data = pd.read_csv("./Data/label_train.csv").iloc[:]
feature_test_data = pd.read_csv("./Data/feature_test.csv").iloc[:]
label_test_data = pd.read_csv("./Data/label_test.csv").iloc[:]

merged_train_files = label_train_data.merge(feature_train_data, how='outer', left_index=True, right_index=True)
merged_test_files = label_test_data.merge(feature_test_data, how='outer', left_index=True, right_index=True)

max_gain = max_gain_feature(merged_train_files.drop("Diabetes_012", axis=1), merged_train_files["Diabetes_012"])
# print(max_gain_feature(merged_files.drop("Diabetes_012", axis=1), merged_files["Diabetes_012"]))

tree = Tree()
tree.build(merged_train_files,max_gain)
tree.print_tree(tree.root)
print(tree.predict(merged_test_files,tree.root))
