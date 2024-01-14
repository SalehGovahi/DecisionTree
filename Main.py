from Calculating import *
from Tree import *

feature_train = pd.read_csv("./Data/feature_train-Copy.csv")
label_train = pd.read_csv("./Data/label_train-Copy.csv")

merged_csv = label_train.merge(feature_train, how='outer', left_index=True, right_index=True)


max_feature_gain = max_gain_feature('./Data/feature_train-Copy.csv', './Data/label_train-Copy.csv')
print(max_feature_gain)
tree = Tree()
tree.add_node(merged_csv, max_feature_gain)
tree.draw_tree()

