import pandas as pd
import math


def entropy(y):
    hist = [list(y).count(i) for i in set(y)]
    ps = [i / len(y) for i in hist]
    return -sum([p * math.log2(p) for p in ps if p > 0])


def gain(y, x):
    original_entropy = entropy(y)
    values = set(x)
    subsets_entropy = 0
    for value in values:
        indices = [i for i, x_value in enumerate(x) if x_value == value]
        subset_y = [y[i] for i in indices]
        subset_entropy = entropy(subset_y)
        subsets_entropy += (len(indices) / len(y)) * subset_entropy
    return original_entropy - subsets_entropy


def calculate_gain(df_features, df_labels):


    # Convert labels dataframe to a 1D list
    y = df_labels.tolist()

    # Calculate gain for each feature
    gain_dict = {}
    for column in df_features.columns:
        x = df_features[column].tolist()
        gain_dict[column] = gain(y, x)

    return gain_dict


def max_gain_feature(features, labels):
    gain_dict = calculate_gain(features, labels)
    max_gain = 0
    max_feature = None
    for k, v in gain_dict.items():
        if v > max_gain:
            max_gain = v
            max_feature = k
    return max_feature
