"""
This function removes a specified item from the data list.
Adds the action, item and index to the history list for use in undo.

params:
    data (list): The list of items
    history (list): A list of user action , item, index.

"""


def remove(data, history):
    item_nr = int(input("Enter the number of the item in the list you'd like to remove\n"))
    try:
        history.append('remove')
        history.append(data[item_nr-1])
        history.append(item_nr-1)
        del data[item_nr-1]

    except IndexError:
        print("index of of bounds")
    except ValueError:
        print("Must be a valid number")
