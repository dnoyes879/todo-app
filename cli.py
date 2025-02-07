from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        #file = open('files/todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos('files/todos.txt')

        #new_todos = []
        #for item in todos:
        #    new_item = item.strip('\n')
        #    new_todos.append(new_item)

        #new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            new_todo = input('Enter a new todo: ')

            todos = get_todos()

            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is invalid')
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) - 1

            todos = get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from the list'
        except IndexError:
            print('There is no item with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command invalid')




