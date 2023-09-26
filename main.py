from controller.todo import Todo
from persistence.file import FileManager
from exception.command import InvalidCommandError
from validator.command import check_command

user_prompt = "Enter add, show, edit, complete or exit:"

stop = True

TODOS_FILE = 'todos.txt'

todo_controller = Todo(file_manager=FileManager(), todos=[])

while stop:
    action = input(user_prompt)
    action = action.strip()
    try:
        if action.startswith('add'):
            item = action[4:]
            check_command(item)
            try:
                todo_controller.add(action)
            except ValueError:
                print("Invalid command")
        elif action.startswith('show'):
            try:
                print(todo_controller.show())
            except ValueError:
                print("Invalid command")
                continue
        elif action.startswith('edit'):
            index = int(action[5:])
            todo_controller.edit(index)
            print("Todos list updated")
        elif action.startswith('complete'):
            index = int(action[9:])
            todo_controller.complete(index)
        elif action.startswith('exit'):
            stop = False
            print('Bye!')
        else:
            print('Command not recognized, enter add, show or exit!')
    except ValueError as e:
        print("Invalid command!")
    except InvalidCommandError as e:
        print(e)
    finally:
        continue


