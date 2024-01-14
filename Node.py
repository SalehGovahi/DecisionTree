class Node:
    def __init__(self, data, parent, is_leaf, feature_name, labels, child):
        self.id = id
        self.is_leaf = is_leaf
        self.parent = parent
        self.data = data
        self.feature_name = feature_name
        self.labels = labels
        self.children.append(child)

