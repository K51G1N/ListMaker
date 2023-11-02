"""
This essentially overrides an item in the list that the user specified with whatever the user enters thereafter
params:
    data (list): The list of items
    history (list): A list of user action , item, index.
"""


def edit(data, history):
    datapoint_nr = input("Enter the number of the item in the list you'd like to edit\n")

    try:
        datapoint_nr = int(datapoint_nr)
        history.append('edit')
        history.append(data[datapoint_nr - 1])
        history.append(datapoint_nr-1)
        updated_item = input("Update the item:\n")
        data[datapoint_nr - 1] = updated_item
        print(history)
    except IndexError:
        print("index of of bounds")
    except ValueError:
        print("Must be a valid number")
    except TypeError:
        print("String and int error")
