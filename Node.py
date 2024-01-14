class Node:
    MAGORITY = 80

    def __init__(self, data, parent, is_leaf, feature_name, child):
        self.id = id
        self.is_leaf = is_leaf
        self.parent = parent
        self.data = data
        self.feature_name = feature_name
        self.children = []
        if child is not None:
            self.children.append(child)

    def is_magority(self):
        lst = self.data["Diabetes_012"].tolist()
        # print(f"lst is {lst}")
        temp = {}
        type = []
        for x in lst:
            if x in type:
                temp[x] += 1
            else:
                temp[x] = 1
        max_key = max(temp, key=temp.get)
        # print(f"magority is {max_key/len(lst)}")
        if (max_key/len(lst)) >= self.MAGORITY:
            self.is_leaf = True
            return True
        else:
            return False

    def add_child(self, child):
        self.children.append(child)

    def get_edges(self):
        edges = [(self, child) for child in self.children]
        for child in self.children:
            edges.extend(child.get_edges())
        return edges
