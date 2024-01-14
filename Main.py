from Calculating import *
from Tree import *

feature_train = pd.read_csv("./Data/feature_train.csv")
label_train = pd.read_csv("./Data/label_train.csv")

print(feature_train["GenHlth"].unique())

merged_csv = label_train.merge(feature_train, how='outer', left_index=True, right_index=True)


max_feature_gain = max_gain_feature('./Data/feature_train.csv', './Data/label_train.csv')
print(max_feature_gain)
tree = Tree()
tree.add_node(merged_csv, max_feature_gain)
tree.draw_tree()

