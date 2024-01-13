class Node:
    def __init__(self, id, isLeaf, feature, children=None, parent=None, data=None, labels=None):
        self.id = id
        self.isLeaf = isLeaf
        self.feature = feature
        self.children = children
        self.parent = parent
        self.data = data
        self.labels = labels

