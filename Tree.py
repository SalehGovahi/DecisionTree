from Node import *
from Calculating import *


class Tree:
    root = Node

    def __init__(self, data, feature_name, labels):
        self.root = Node(data, None, False, feature_name, labels)
        merged_csv = labels.merge(data, how='outer', left_index=True, right_index=True)
        # print(merged_csv)
        unique_values = merged_csv[feature_name].unique()
        data_frame_each_unique = {value: merged_csv[merged_csv[feature_name] == value] for value in unique_values}

        for value, data_frame in data_frame_each_unique.items():
            print(f"DataFrame for GenHlth = {value}:")
            print(data_frame)

        columns_to_filter = ["HighBP", "HighChol", "CholCheck", "Smoker", "Stroke", "HeartDiseaseorAttack",
                            "PhysActivity", "Fruits",
                            "Veggies", "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth", "DiffWalk",
                            "Sex", "Education", "Income"]

        # if feature_name in columns_to_filter:
        #     columns_to_filter.remove(feature_name)

        for value, data_frame in data_frame_each_unique.items():
            print(calculate_gain_column(merged_csv[columns_to_filter],merged_csv["Diabetes_012"]))
            print(max_gain_feature_column(merged_csv[columns_to_filter],merged_csv["Diabetes_012"]))
            # print(data_frame)

    # def add_children(self,data, parent,feature_name, labels):
