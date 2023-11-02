from logic.add import add
from logic.remove import remove
from logic.show import show
from logic.edit import edit
from logic.undo import undo
from logic.save import save
import os

def start(data, history):
    user_prompt = "Enter add, show, edit or remove, undo or exit: \n"
    while True:
        user_action = input(user_prompt)
        match user_action:
            case 'add':
                still_adding = True
                while still_adding is True:
                    still_adding = add(data, history)
                    show(data)
            case 'show':
                show(data)
            case 'edit':
                edit(data, history)
                show(data)
            case 'remove':
                remove(data, history)
                show(data)
            case 'undo':
                undo(data, history)
                show(data)
            case 'exit':
                user_answer = input("Would you like to save this to a textfile? y \n")
                if user_answer.lower() == 'y':
                    filename = input("Enter the name of the file \n")
                    choice = 'n'
                    while os.path.isfile(filename):
                        print(f"{filename} already exists! Would you like to save over it 'y/n'?")
                        choice = input()
                        if choice == 'y':

                            save(data, filename)
                            history_filename = "history_" + filename
                            save(history, history_filename)
                            break
                        else:
                            filename = input("Enter the name of the file \n")
                    save(data, filename)
                    history_filename = "history_" + filename
                    save(history, history_filename)
                break
