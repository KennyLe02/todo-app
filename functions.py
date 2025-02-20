FILEPATH = 'files/todos.txt'

def getTodos(filepath = FILEPATH):
    #Read a text file and return list of to-do items
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath= FILEPATH):

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    #we don't return anything because its more of a procedure
    #it doesn't need to return any values