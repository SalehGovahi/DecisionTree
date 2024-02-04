import pandas as pd
from Calculating import *
from Tree import *

feature_train_data = pd.read_csv("./Data/feature_train.csv").iloc[:]
label_train_data = pd.read_csv("./Data/label_train.csv").iloc[:]
feature_test_data = pd.read_csv("./Data/feature_test.csv").iloc[:]
label_test_data = pd.read_csv("./Data/label_test.csv").iloc[:]
dataset_all = pd.read_csv("./Data/diabetes_012_health_indicators_BRFSS2015.csv")

merged_train_files = label_train_data.merge(feature_train_data, how='outer', left_index=True, right_index=True)
merged_test_files = label_test_data.merge(feature_test_data, how='outer', left_index=True, right_index=True)
max_gain = max_gain_feature(merged_train_files.drop("Diabetes_012", axis=1), merged_train_files["Diabetes_012"])

tree = Tree()
tree.build(merged_train_files,max_gain)
tree.print_tree(tree.root)

#print(tree.get_depth(tree.root))
#print(len(tree.predict(feature_test_data)))
#print(label_test_data["Diabetes_012"].tolist())
#print(tree.predict(feature_test_data))
accuracy = tree.calculate_accuracy(label_test_data["Diabetes_012"].tolist(), tree.predict(feature_test_data))
print(f"Accuracy is {accuracy}")
depth_accuracy = tree.calculate_accuracy(label_test_data["Diabetes_012"].tolist(),tree.predict_depth(feature_test_data,1))
print(f"Accuracy is {depth_accuracy}")