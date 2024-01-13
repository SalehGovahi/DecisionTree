import pandas as pd
import math

def entropy(y):
    hist = [list(y).count(i) for i in set(y)]
    ps = [i / len(y) for i in hist]
    return -sum([p * math.log2(p) for p in ps if p > 0])

def gain(y, x):
    # Calculate the original entropy
    original_entropy = entropy(y)

    # Get unique values of feature
    values = set(x)

    # Calculate the entropy of each subset
    subsets_entropy = 0
    for value in values:
        indices = [i for i, x_value in enumerate(x) if x_value == value]
        subset_y = [y[i] for i in indices]
        subset_entropy = entropy(subset_y)
        subsets_entropy += (len(indices) / len(y)) * subset_entropy

    # Return the gain
    return original_entropy - subsets_entropy

def read_files_and_calculate_gain(features_file_path, labels_file_path):
    # Read features and labels into dataframes
    df_features = pd.read_csv(features_file_path)
    df_labels = pd.read_csv(labels_file_path)

    # Ensure that the labels are a single column dataframe
    assert df_labels.shape[1] == 1, "Labels file should only have one column"

    # Convert labels dataframe to a 1D list
    y = df_labels.iloc[:, 0].tolist()

    # Calculate gain for each feature
    gain_dict = {}
    for column in df_features.columns:
        x = df_features[column].tolist()
        gain_dict[column] = gain(y, x)

    return gain_dict

def max_gain_feature(features_file_path, labels_file_path):
    gain_dict = read_files_and_calculate_gain(features_file_path,labels_file_path)
    max_gain = 0
    max_feature = None
    for k, v in gain_dict.items():
        if v > max_gain:
            max_gain = v
            max_feature = k
    return max_feature


def calculate_gain_column(feature,label):
    # Ensure that the labels are a single column dataframe
    assert label.shape[1] == 1, "Labels file should only have one column"

    # Convert labels dataframe to a 1D list
    y = label.iloc[:, 0].tolist()

    # Calculate gain for each feature
    gain_dict = {}
    for column in feature.columns:
        x = feature[column].tolist()
        print(column)
        gain_dict[column] = gain(y, x)

    return gain_dict