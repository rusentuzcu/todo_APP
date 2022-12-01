
FILEPATH = "todos.txt"
def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())
    