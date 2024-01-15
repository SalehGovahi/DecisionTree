class Node:
    def __init__(self, data, feature_name, parent, child):
        self.data = data
        self.feature_name = feature_name
        self.parent = parent
        self.children = []
        self.child = child  # Add this line

    def add_child(self, node):
        self.children.append(node)


    def is_majority(self):
        lst = self.data["Diabetes_012"].tolist()
        temp = {}
        for x in lst:
            if x in temp:
                temp[x] += 1
            else:
                temp[x] = 1
        max_key = max(temp, key=temp.get)
        if (temp[max_key]/len(lst)) * 100 >= self.MAJORITY:
            self.is_leaf = True
            return True
        else:
            return False


    def get_edges(self):
        edges = [(self, child) for child in self.children]
        for child in self.children:
            edges.extend(child.get_edges())
        return edges
