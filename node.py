class Node:
    def __init__(self,name,node_type):
        self.name = name
        self.node_type = node_type
        self.parent = None
        self.children = []
        self.content = ""