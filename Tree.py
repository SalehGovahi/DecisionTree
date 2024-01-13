from Node import *
from Calculating import *


class Tree:
    root = Node
    def __init__(self, data, feature_name, labels):
        self.root = Node(data, None, False, feature_name, labels)
        unique_values = data[feature_name].unique()
        data_frame_each_unique = {value: data[data[feature_name] == value] for value in unique_values}

        for value, data_frame in data_frame_each_unique.items():
            print(f"DataFrame for GenHlth = {value}:")
            print(data_frame)

        data = {
            'Diabetes_012': []
        }
        index_list = []
        for value, data_frame in data_frame_each_unique.items():
            index_list.append(data_frame.index.tolist())
        label_indexes = []
        print(index_list)
        for x in index_list:
            value = labels.loc[x, 'Diabetes_012']
            value = value.item()
            label_indexes.append(value)
            print("label indexes")
            print(label_indexes)
        print(label_indexes)
        # print(label_indexes)
        # data['Diabetes_012'] = index_list
        #
        # label_data_frame = pd.DataFrame(data)
        # print(label_data_frame)
        # result = {}
        # for value, data_frame in data_frame_each_unique.items():
        #     result[value] = calculate_gain_column(data_frame, label_data_frame)
        # print(result)


    # def add_children(self,data, parent,feature_name, labels):

