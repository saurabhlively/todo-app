def get_todos(filepath='todos.txt'):
    """Read a text file and return the todos list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath='todos.txt'):
    """Write a todos list to a file"""
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())