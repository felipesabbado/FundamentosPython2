# The os module: LAB
# Creating test directory structure
"""
tree
    c
        other_courses
            cpp
            python
    cpp
        other_courses
            c
            python
    python
        other_courses
            c
            cpp
"""
import os

def find(path, dir):
    try:
        os.chdir(path)
    except OSError:
        # Doesn't process a file that isn't a directory.
        return

    current_dir = os.getcwd()
    for entry in os.listdir("."):
        if entry == dir:
            print(os.getcwd() + "\\" + dir)
        find(current_dir + "\\" + entry, dir)


# Main program
find("./tree", "python")