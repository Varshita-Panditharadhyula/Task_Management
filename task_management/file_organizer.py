from data import file_details  # Importing the file_details dictionary from data.py

# Implement the sorting logic based on criteria
def display_files():
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("File Viewer")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Type", "Size", "Date Modified")
    tree.column("#0", width=200)
    tree.column("Type", width=100)
    tree.column("Size", width=100)
    tree.column("Date Modified", width=150)

    tree.heading("#0", text="File Name")
    tree.heading("Type", text="Type")
    tree.heading("Size", text="Size")
    tree.heading("Date Modified", text="Date Modified")

    for file_name, details in file_details.items():
        file_size = str(details.get('file_size', 'N/A')) + "KB" if 'file_size' in details else 'N/A'
        tree.insert("", "end", text=file_name, values=(details.get('file_type', 'N/A'),
                                                       file_size,
                                                       details.get('date_modified', 'N/A')))

    tree.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
def sort_files(file_list, criteria):
    if criteria == 'file_type':
        return sorted(file_list, key=lambda x: file_details[x]['file_type'])
    elif criteria == 'file_size':
        return sorted(file_list, key=lambda x: file_details[x]['file_size'])
    elif criteria == 'date_modified':
        return sorted(file_list, key=lambda x: file_details[x]['date_modified'])
    else:
        return file_list

def add_file(filename, details):
    file_details[filename] = details

def retrieve_file(filename):
    return file_details.get(filename, "File not found")

import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

def add_file(filename, details):
    with open('data.py', 'r') as file:
        data = file.readlines()

    for idx, line in enumerate(data):
        if 'file_details = {' in line:
            indent = line.index('file_details')
            data.insert(idx + 1, f"{' ' * (indent + 4)}'{filename}': {details},\n")
            break

    with open('data.py', 'w') as file:
        file.writelines(data)
    file_details[filename]=details

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()  # Open file dialog for file selection

    if file_path:
        file_name = os.path.basename(file_path)  # Extract file name
        file_size = os.path.getsize(file_path)  # Get file size
        file_type = os.path.splitext(file_path)[-1]  # Get file extension
        date_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')  # Get modification date

        details = {
            'file_type': file_type,
            'file_size': file_size,
            'date_modified': date_modified
        }

        add_file(file_name, details)  # Add file details to file_details dictionary
        print(f"File '{file_name}' details added successfully:\n{details}")

def user_interface():
    print("Welcome to File Organizer!")
    while True:
        print("\n1. Sort Files\n2. Display Files\n3. Retrieve File Details\n4. Add File\n5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            criteria = input("Sort files by (file_type, file_size, date_modified): ")
            sorted_files = sort_files(file_details.keys(), criteria)
            print("Files sorted:")
            for file_name in sorted_files:
                details = file_details[file_name]
                print(f"File: {file_name}, Type: {details.get('file_type', 'N/A')}, Size: {details.get('file_size', 'N/A')}KB, Date Modified: {details.get('date_modified', 'N/A')}")
        elif choice == '2':
            display_files()
        elif choice == '3':
            file_name = input("Enter file name to retrieve details: ")
            details = retrieve_file(file_name)
            if details != "File not found":
                print(f"File: {file_name}, Type: {details.get('file_type', 'N/A')}, Size: {details.get('file_size', 'N/A')}KB, Date Modified: {details.get('date_modified', 'N/A')}")
            else:
                print("File not found.")
        elif choice == '4':
            select_file()
        elif choice == '5':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Try again.")
