# Virtual File system

## Description
A tree-based Virtual File system implemented in Python. It is a simple simulation of how users can navigate and manage files and folders through a terminal-basef interface.

# Data Structures
- Tree
- Parent-Child relationship
- Depth-First Search(DFS)
- Recursion

## Features

- Create files/folders
- Navigate between folders
- Read and Write files
- Delete files and folders
- Rename files and folders
- Search for files and folders
- Display the complete directory tree using DFS
- Display file and folder information
- Display the current working path
- Clear the terminal
- Persistent storage using JSON

# How to run

python main.py

## Commands

create_folder <name>
create_file <name>
open <file_name>
read_info <name>
change_folder <name>
print_working_folder
write <name> <content>
delete <name>
rename <old_name> <new_name>
find <name>
list
back
tree
help
logout

## Tree Command

The tree command displays the complete file system hierarchy starting from the root directory.

Example:

📁 root
└── 📁 Documents
    ├── 📄 notes.txt
    └── 📄 resume.txt
└── 📁 Projects
    └── 📄 vfs.txt
└── 📄 photo.txt

The tree is displayed using a recursive Depth-First Search (DFS) traversal.

## Persistence

The file system is automatically loaded from filesystem.json when the program starts.

When logout is used, the current file system is saved to filesystem.json, allowing the data to be available the next time the program is run.