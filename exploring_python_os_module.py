# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.

import os

def list_directory_contents(path):
    directory_list = os.listdir(path)
    print(f"The following directories and files were found in '{path}'")
    for directory in directory_list:
        print(directory)
    return

while True:
    try:
        user_input = input("Enter a path to print the contents:\n(Type 'quit' to exit)\n")
        if user_input == "quit":
            break
        else:
            list_directory_contents(user_input)
    except FileNotFoundError:
        print("File Not Found Error: Path does not exist. Please enter a valid path.")
    except PermissionError:
        print("Permission Error: You do not have permissions for this file. Please try another file.")
    except OSError:
        print("OS Error: Please make sure to remove quotations from beginning and end of path.")
    except Exception:
        print("Unknown Error: Please try a different path.") 
