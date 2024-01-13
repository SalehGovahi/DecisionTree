from Calculating import *
from Tree import *

feature_train = pd.read_csv("./Data/feature_train-Copy.csv")
label_train = pd.read_csv("./Data/label_train-Copy.csv")

max_feature_gain = max_gain_feature('./Data/feature_train.csv', './Data/label_train.csv')
print(max_feature_gain)
tree = Tree(feature_train, max_feature_gain, label_train)

