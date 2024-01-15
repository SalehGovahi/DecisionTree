import numpy as np

from Node import *
from Calculating import *


class Tree:

    def __init__(self):
        self.root = None

    def add_node(self, data, feature_name, parent, child):
        node = Node(data, feature_name, parent, child)  # Pass child here
        if parent is not None:
            parent.add_child(node)
        return node

    def build_tree(self, node ,data):
        if len(data["Diabetes_012"].unique()) == 1:
            return

        unique_values = data[node.feature_name].unique()
        data_frame_each_unique = {value: data[data[node.feature_name] == value] for value in unique_values}
        data = data.drop(node.feature_name, axis=1)

        result = {}
        for k, v in data_frame_each_unique.items():
            gain1 = max_gain_feature(data.drop("Diabetes_012", axis=1), data["Diabetes_012"])
            if gain1 is None:
                continue
            data_frame = {"data_frame": v}
            gain = {"gain": gain1}
            result[k] = [gain, data_frame]

        for k, v in result.items():
            child_node = self.add_node(v[1]["data_frame"], v[0]["gain"], node, k)
            self.build_tree(child_node, v[1]["data_frame"])

    def build(self, data, feature_name):
        self.root = self.add_node(data, feature_name, None, None)
        self.build_tree(self.root, data)

    def print_tree(self, node, depth=0):
        print(' ' * depth + str(node.feature_name))
        for child in node.children:
            self.print_tree(child, depth + 1)

    def predict(self, data, node):
        if len(node.children) == 0:
            return node.feature_name

        for child in node.children:
            # Add validation here
            if child.child in data.columns and child.feature_name == data[child.child]:
                return self.predict(data, child)

        return np.nan


