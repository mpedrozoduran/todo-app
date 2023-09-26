class TodoListIndexError(Exception):
    def __init__(self, message: str = "Invalid index"):
        super().__init__(message)