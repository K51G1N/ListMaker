"""Main module for running the program."""

from logic.start import start
from src.welcome import welcome
from src.load_previous_list import load_previous_list

def main():
    """
    The main function to start the program.

    This function displays a welcome message, loads data and history from previous lists,
    and starts the main program using the loaded data and its history.
    """
    welcome()
    data, history = load_previous_list()
    start(data, history)

if __name__ == '__main__':
    main()
