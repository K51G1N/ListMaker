"""
This method reads a file and then strips it of any newline characters
:param
    filename (string): name of file to be run
:return
    data (list): the contents of the file read in.
"""

import os


def load(filename):
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = [line.strip() for line in file.readlines()]
    else:
        data = []
    return data
