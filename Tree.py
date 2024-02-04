from Node import *
from Calculating import *


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, data, feature_name, parent, feature_value):
        node = Node(data, feature_name, parent, feature_value)
        if parent is not None:
            parent.add_child(node)
        return node

    def build_tree(self, node, data):
        if len(data["Diabetes_012"].unique()) == 1:
            return

        unique_values = data[node.feature_name].unique()
        data_frame_each_unique = {value: data[data[node.feature_name] == value] for value in unique_values}
        data = data.drop(node.feature_name, axis=1)

        for k, v in data_frame_each_unique.items():
            gain1 = max_gain_feature(data.drop("Diabetes_012", axis=1), data["Diabetes_012"])
            if gain1 is None:
                continue
            data_frame = {"data_frame": v}
            gain = {"gain": gain1}
            child_node = self.add_node(data_frame["data_frame"], gain["gain"], node, k)
            self.build_tree(child_node, data_frame["data_frame"])

    def build(self, data, feature_name):
        self.root = self.add_node(data, feature_name, None, None)
        self.build_tree(self.root, data)

    def print_tree(self, node, depth=0):
        print('    ' * depth + str(node.feature_name) + " : " + str(list(node.diabetes_data)))
        for child in node.children:
            self.print_tree(child, depth + 1)

    def get_depth(self, node, depth=0):
        if not node.children:
            return depth
        max_child_depth = max(self.get_depth(child, depth + 1) for child in node.children)
        return max_child_depth

    def predict(self, data):
        predictions = [self.predict_instance(instance, self.root) for _, instance in data.iterrows()]
        return predictions

    def predict_instance(self, instance, node):

        if not node.children:
            return node.diabetes_data.mode()[0]  # return the most common label


        for child in node.children:
            if instance[node.feature_name] == child.feature_value:
                return self.predict_instance(instance, child)


        return None

    def predict(self, data):
        predictions = [self.predict_instance(instance, self.root) for _, instance in data.iterrows()]
        return predictions  # returns a list of predictions

    def calculate_accuracy(self, actual, predicted):
        if len(actual) != len(predicted):
            raise ValueError("The length of actual values and predicted values don't match.")
        correct = sum(a == p for a, p in zip(actual, predicted))
        accuracy = correct / len(actual)
        return accuracy*100

    def predict_instance_depth(self, instance, node, max_depth, current_depth=0):
        # base case: if node is a leaf node or max_depth is reached
        if not node.children or current_depth == max_depth:

            if node.diabetes_data.empty or node.diabetes_data is None:
                return None
            return node.diabetes_data.mode()[0]  # return the most common label


        for child in node.children:
            if instance[node.feature_name] == child.feature_value:
                return self.predict_instance_depth(instance, child, max_depth, current_depth + 1)


        return None

    def predict_depth(self, data, max_depth):
        predictions = [self.predict_instance_depth(instance, self.root, max_depth) for _, instance in data.iterrows()]
        return predictions  # returns a list of predictions to given depth