from exception.index import TodoListIndexError
from persistence.file import FileManager

class Todo:

    def __init__(self, file_manager: FileManager, todos: list):
        self.file_manager = file_manager
        self.todos = todos

    def add(self, action: str):
        try:
            todo = action[4:]
            self.todos.append(todo)
            self.file_manager.append(todo)
        except ValueError as e:
            raise e

    def complete(self, index: int):
        try:
            self.todos = self.file_manager.get()
            self.todos.pop(index)
            self.file_manager.write(self.todos)
        except ValueError as e:
            raise e

    def show(self) -> list:
        res = []
        try:
            self.todos = self.file_manager.get()
            for index, item in enumerate(self.todos, 1):
                new_item = item.strip('\n')
                res.append(f"{index}:{new_item}")
            return res
        except ValueError as e:
            raise e

    def edit(self, index: int):
        self.todos = self.file_manager.get()
        ltodos = len(self.todos)
        if type(index) == int and int(index) > ltodos or int(index) < 0:
            raise TodoListIndexError("Enter a correct index!")
        new_todo = input("Enter the new value:")
        self.todos[int(index)] = new_todo + '\n'
        self.file_manager.write(self.todos)