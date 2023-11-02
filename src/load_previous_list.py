"""
This allows the user to enter the name of a file containing a list.
"""

import os

from logic.load import load
from logic.show import show

def load_previous_list():
    """
    Load previous list loads the saved data.txt and then the history
    """
    choice = input("Would you like to load a previous list? 'y'\n")
    if choice == 'y':
        while choice == 'y':
            filename = input("Enter the name of the file\n")
            if os.path.isfile(filename):
                data = load(filename)
                history = load("history_"+filename)
                choice = 'n'
            else:
                print("That file does not exist")
                choice = input("Would you like to retype the name of the file? y/n\n")

        if len(data) == 0:
            print("the file was empty")
        show(data)
    else:
        data = []
        history = []
    return data, history
