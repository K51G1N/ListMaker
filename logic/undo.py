"""
This module performs the opposite action of what was recorded in history
params:
    data (list): The list of items
    history (list): A list of user action , item, index.
"""


def undo(data, history):
    try:
        index = history[-1]
        item = history[-2]
        action = history[-3]

        index = int(index)
        match action:
            case 'remove':
                start_data = data[0:index]
                end_data = data[index:]
                start_data.append(item)
                start_data.extend(end_data)
                data.clear()
                data.extend(start_data)
            case 'edit':
                data[index] = item
            case 'add':
                del data[index]

        del history[-1]
        del history[-1]
        del history[-1]
    except IndexError:
        print(history)
        print("Nothing to undo")
