"""
This calls the welcome method, loads an existing list and
initialises the data & history either from the list or blank

"""

from logic.start import start
from src.welcome import welcome
from src.load_previous_list import load_previous_list


def main():
    """
    This starts our code
    """
    welcome()
    data, history = load_previous_list()
    start(data, history)


if __name__ == '__main__':
    main()
