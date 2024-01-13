import math

from Node import *


# class TreeNode:
#     def __init__(self, base):
#         self.base = base
#         self.label = ""
#
#     # def add_leaf (self, leaf_label,data):


class Tree:

    def calculate_parent_entropy(self, data):
        column_entropy = 0
        types = []
        for value in data['Diabetes_012']:
            if value not in types:
                types.append(value)
                probability = data['Diabetes_012'].value_counts()[value] / len(data['Diabetes_012'])

                contribution = probability * math.log2(probability)

                column_entropy -= contribution
        return column_entropy

    def calculate_features_entropy(self, data, filters_to_delete = None):
        column_entropy = 0
        result = {}
        types = []
        features_column_name = ["HighBP", "HighChol", "CholCheck", "Smoker", "Stroke", "HeartDiseaseorAttack",
                                "PhysActivity", "Fruits",
                                "Veggies", "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth", "DiffWalk",
                                "Sex", "Education", "Income"]
        if filters_to_delete is not  None:
            for filter_to_delete in filters_to_delete:
                if filter_to_delete in features_column_name:
                    self.remove_value(features_column_name, filter_to_delete)
        for column_name in features_column_name:
            for value in data[column_name]:
                if value not in types:
                    types.append(value)
                    probability = data[column_name].value_counts()[value] / len(data[column_name])
                    # print(probability)
                    # print(math.log2(probability))
                    contribution = probability * math.log2(probability)
                    # print(f"{column_name} , {value} , {contribution}")
                    column_entropy -= contribution
            result[column_name] = column_entropy
            column_entropy = 0
        return result

    def calculate_gain(self, labels, column_data):
        result = {}
        parent_entropy = self.calculate_parent_entropy(labels)
        for k, v in column_data.items():
            result[k] = parent_entropy - v
        return result

    def find_max_gain(self, labels, column_data):
        base_file = self.calculate_gain(labels, column_data)
        max_gain = 0
        max_feature = ""
        for k, v in column_data.items():
            if v > max_gain:
                max_gain = v
                max_feature = k
        return max_feature

    def create_child(self, data, labels, feature_name, filters_to_delete = None):
        length = len(data[feature_name])
        result = {}
        filters_to_delete = []
        filters_to_delete = filters_to_delete
        for i in range(len(data[feature_name])):
            if data[feature_name][i] in result.keys():
                result[data[feature_name][i]].append(i)
            else:
                result[data[feature_name][i]] = []
                result[data[feature_name][i]].append(i)
        print(result)
        for key, value in result.items():
            result[key] = self.calculate_parent_entropy_sub_leaf(value)
        print(result)
        print(self.calculate_features_entropy(data, feature_name))
        print(self.find_max_gain(labels, result))
        if filters_to_delete is not None:
            filters_to_delete.append(self.find_max_gain(labels, self.calculate_features_entropy(data)))
        else:
            filters_to_delete.append(self.find_max_gain(labels, self.calculate_features_entropy(data)))
        print(filters_to_delete)
        # self.create_child(data, labels, self.find_max_gain(labels, self.calculate_features_entropy(data, feature_name)),filters_to_delete)

    def calculate_parent_entropy_sub_leaf(self, data):
        column_entropy = 0
        types = []
        for value in data:
            if value not in types:
                repetition = self.count_repetition(data, value)
                types.append(value)
                probability = repetition / len(data)

                contribution = probability * math.log2(probability)

                column_entropy -= contribution
        return column_entropy

    def count_repetition(self, list1, item):
        count = 0
        for i in list1:
            if i == item:
                count += 1
        return count

    def remove_value(self, list1, item):
        for i in range(len(list1)):
            if list1[i] == item:
                del list1[i]
                break

    def create_tree(self, root_feature, data, labels):
        id_counter = 0
        children = []
        root = Node(id_counter, False, root_feature, children, None, data, labels)
