from Node import *
from Calculating import *
import networkx as nx
import matplotlib.pyplot as plt


def add_children(parent, child):
    parent.add_child(child)
class Tree:
    root = None
    parent_default = None
    this_node = None

    def __init__(self):
        self.root = None

    def add_node(self, merged_csv, feature_name):
        columns_to_filter = ["HighBP", "HighChol", "CholCheck", "Smoker", "Stroke", "HeartDiseaseorAttack",
                             "PhysActivity", "Fruits",
                             "Veggies", "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth", "DiffWalk",
                             "Sex", "Education", "Income"]
        if self.root is None:
            self.this_node = Node(merged_csv, self.parent_default, False, feature_name, None)
            self.root = self.this_node
            unique_values = merged_csv[feature_name].unique()
            data_frame_each_unique = {value: merged_csv[merged_csv[feature_name] == value] for value in unique_values}

            if feature_name in columns_to_filter:
                columns_to_filter.remove(feature_name)

            for value, data_frame in data_frame_each_unique.items():
                max_gain_feature_name = max_gain_feature_column(merged_csv[columns_to_filter],
                                                                merged_csv["Diabetes_012"])
                self.parent_default = self.root
                self.this_node = Node(data_frame, self.parent_default, False, max_gain_feature_name, None)
                self.parent_default.add_child(self.this_node)

            for child in self.root.children:
                if child.is_magority() is False:
                    for value, data_frame in data_frame_each_unique.items():
                        max_gain_feature_name = max_gain_feature_column(merged_csv[columns_to_filter],
                                                                        merged_csv["Diabetes_012"])
                        self.parent_default = child
                        self.this_node = Node(data_frame, self.parent_default, False, max_gain_feature_name, None)
                        self.parent_default.add_child(self.this_node)

    def draw_tree(self):
        try:
            G = nx.DiGraph()
            edges = self.root.get_edges()
            G.add_edges_from(edges)

            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, font_weight='bold')
            plt.savefig("tree.png")
        except Exception as e:
            print(f"An error occurred: {e}")