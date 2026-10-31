import json
from node import Node

class FileSystem:
    def __init__(self):
        self.root = Node("root","folder")
        self.current = self.root
        
    def create_folder(self,name):
        for child in self.current.children:
            if child.name == name:
                print("This file or folder name already exists")
                return
        
        folder = Node(name,"folder")
        folder.parent = self.current
        self.current.children.append(folder)
    
    def list_contents(self):
        for child in self.current.children:
            if child.node_type == "folder":
                icon = "📁"
            else:
                icon = "📄"
            
            print(icon, child.name)
            
    def change_folder(self,name):
        for child in self.current.children:
            if child.name == name and child.node_type == "folder":
                self.current = child
                return
        
        print("Folder Not found.")

    def back(self):
        if self.current.parent is not None:
            self.current = self.current.parent
        else:
            print("Already at root.")
    
    def print_working_folder(self):
        path = []
        current = self.current
        
        while current is not None:
            path.append(current.name)
            current = current.parent
        
        path.reverse()
        
        print("📁/"+"/".join(path))
        
    def create_file(self,name):
        for child in self.current.children:
            if child.name == name:
                print("This file or folder name already exists")
                return
        
        file = Node(name,"file")
        file.parent = self.current
        self.current.children.append(file)
    
    def open(self,name):
        for child in self.current.children:
            if child.name == name and child.node_type == "file":
                print(child.content)
                return
        
        print("File not found.")
    
    def write(self,name,content):
        for child in self.current.children:
            if child.name == name and child.node_type == "file":
                child.content = content
                return
        
        print("File Not Found.")
    
    def read_info(self,name):
        for child in self.current.children:
            if child.name == name:
                print("Name:" , child.name)
                print("Type:",child.node_type)
                
                path = []
                current = child
                
                while current is not None:
                    path.append(current.name)
                    current = current.parent
                
                path.reverse()
                
                print("Path:","/"+"/".join(path))
                
                if child.node_type == "file":
                    print("Size:",len(child.content),"bytes")
                else:
                    print("Items:", len(child.children))
                
                return
        print("File or Folder not found.")
    
    def delete(self,name):
        for child in self.current.children:
            if child.name == name:
                self.current.children.remove(child)
                return
        
        print("File or Folder not found.")
        
    def rename(self,current_name,new_name):
        for child in self.current.children:
            if child.name == current_name:
                child.name = new_name
                return
            
        print("File or Folder not Found.")
        
    def find(self,node,name):
        if node.name == name:
            path = []
            current = node
            
            while current is not None:
                path.append(current.name)
                current = current.parent
            path.reverse()
            return "/"+"/".join(path)
        
        for child in node.children:
            result = self.find(child,name)
            
            if result is not None:
                return result
        return None
    
    def find_node(self,name):
        result = self.find(self.root,name)
        
        if result is not None:
            print("Found:",result)
        
        else:
            print("File or folder not found")
            
    def node_to_dict(self,node):
        data = {
            "name":node.name,
            "node_type":node.node_type
        }
        
        if node.node_type == "file":
            data["content"] = node.content
        else:
            data["children"] = []
            
            for child in node.children:
                data["children"].append(self.node_to_dict(child))
        return data
        
    
    def save(self):
        data = self.node_to_dict(self.root)
        
        with open("filesystem.json","w") as file:
            json.dump(data,file,indent=4)
            
    def dict_to_node(self,data,parent = None):
        node = Node(data["name"],data["node_type"])
        node.parent = parent
        
        if node.node_type == "file":
            node.content = data["content"]
        else:
            for child_data in data["children"]:
                child = self.dict_to_node(child_data,node)
                node.children.append(child)
        
        return node
    
    def load(self):
        try:
            with open("filesystem.json","r") as file:
                data = json.load(file)
                
                self.root = self.dict_to_node(data)
                self.current = self.root
        
        except FileNotFoundError:
            pass
        
    def tree(self, node=None, level=0):
        if node is None:
            node = self.root

        if level == 0:
            print("📁", node.name)

        for child in node.children:
            if child.node_type == "folder":
                icon = "📁"
            else:
                icon = "📄"

            print("    " * level + "└── " + icon + " " + child.name)

            if child.node_type == "folder":
                self.tree(child, level + 1)