class Node:
    def __init__(self, data, feature_name, parent, feature_value):
        self.data = data
        self.feature_name = feature_name
        self.parent = parent
        self.feature_value = feature_value
        self.children = []
        self.diabetes_data = data["Diabetes_012"] if "Diabetes_012" in data.columns else None

    def add_child(self, node):
        self.children.append(node)

    def get_edges(self):
        edges = [(self, child) for child in self.children]
        for child in self.children:
            edges.extend(child.get_edges())
        return edges


