import sys
import os
from filesystem import FileSystem

fs = FileSystem()
fs.load()

def help():
    print("tree")
    print("create_folder <name>")
    print("create_file <name>")
    print("open <file_name>")
    print("read_info <name>")
    print("list")
    print("change_folder <name>")
    print("back")
    print("print_working_folder")
    print("write <name> <content>")
    print("delete <name>")
    print("rename <old_name> <new_name>")
    print("find <name>")
    print("help")
    print("clear")
    print("logout")
    
def get_current_path():
    path = []
    current = fs.current
    
    while current is not None:
        path.append(current.name)
        current = current.parent
        
    path.reverse()
    return "/"+"/".join(path)

def main():
    while True:
        command = input(f"VFS:{get_current_path()}$ ").strip()
        
        parts = command.split()
        
        if command == "logout":
            fs.save()
            sys.exit()
            
        elif not parts:
            continue
        
        elif parts[0] == "create_folder" and len(parts) == 2:
            fs.create_folder(parts[1])
        
        elif parts[0] == "create_file" and len(parts) == 2:
            fs.create_file(parts[1])
        
        elif parts[0] == "open" and len(parts) == 2:
            fs.open(parts[1])
        
        elif parts[0] == "read_info" and len(parts) == 2:
            fs.read_info(parts[1])
        
        elif parts[0] == "list" and len(parts) == 1:
            fs.list_contents()
        
        elif parts[0] == "change_folder" and len(parts) == 2:
            fs.change_folder(parts[1])
        
        elif parts[0] == "back" and len(parts) == 1:
            fs.back()
        
        elif parts[0] == "print_working_folder" and len(parts) == 1:
            fs.print_working_folder()
        
        elif parts[0] == "write" and len(parts) >= 3:
            fs.write(parts[1]," ".join(parts[2:]))
        
        elif parts[0] == "delete" and len(parts) == 2:
            fs.delete(parts[1])
        
        elif parts[0] == "rename" and len(parts) == 3:
            fs.rename(parts[1],parts[2])
        
        elif parts[0] == "find" and len(parts) == 2:
            fs.find_node(parts[1])
        
        elif parts[0] == "help" and len(parts) == 1:
            help()
        
        elif parts[0] == "tree" and len(parts) == 1:
            fs.tree()
            
        elif parts[0] == "clear" and len(parts) == 1:
            os.system("cls" if os.name == "nt" else "clear")
        
        else:
            print("Enter a valid command.")
            
if __name__ == "__main__":
    main()