"""
This method adds to the data list and the history. Recording the data added. Recording the action performed
params:
    data (list): The list of items
    history (list): A list of user action , item, index.
"""


def add(data, history):
    datapoint = input("Enter an item or 'q' to stop:\n")
    if datapoint == 'q':
        return datapoint
    data.append(datapoint)
    history.append('add')
    history.append(datapoint)
    history.append(len(data) - 1)
    return True
