
TODOS_FILE = 'todos.txt'

class FileManager:

    def append(self, text: str):
        try:
            with(open(TODOS_FILE, 'a+') as fh):
                todos = fh.readlines()
                todos.append(text)
                fh.writelines(text + '\n')
        except Exception as e:
            raise e

    def write(self, items: list):
        try:
            with(open(TODOS_FILE, 'w') as fh):
                fh.writelines(items)
        except Exception as e:
            raise e

    def get(self):
        with(open(TODOS_FILE, 'r') as fh):
            return fh.readlines()