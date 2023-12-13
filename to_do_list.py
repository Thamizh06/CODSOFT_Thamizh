# run the code in any IDE like VS code to run the program.
# Using this code we can create a set of tasks and perform the following actions: add, list, mark,unmark, delete, edit, quit
def print_task(ind,task):

    print(f"[{ind}{'✓' if task['completed'] else '☐'} {task['description']}")


def add_task(task_description):
    tasks.append({'description': task_description, 'completed': False})


def mark_task_as_completed(task_index):
    tasks[task_index]['completed'] = True

def mark_task_as_not_completed(task_index):
    tasks[task_index]['completed'] = False


def delete_task(task_index):
    tasks.pop(task_index)


def print_tasks():
    m = []
    for ind,task in enumerate(tasks):
        print_task(ind,task)
        m.append(ind)
    maxi = max    


def edit_task(task_index, new_description):
    tasks[task_index]['description'] = new_description


tasks = []

while True:
    maxi = len(tasks)-1

    action = input("Enter an action (add, list, mark,unmark, delete, edit, quit): ")
    
    if action == "add":
        task_description = input("Enter task description: ")
        add_task(task_description)

    elif action == "list":
        print_tasks()

    elif action == "mark":
        print_tasks()
        task_index = int(input("Enter task index: "))
        while task_index >maxi:
            print("Index is out of range, please enter the looking available in the tasks")
            task_index = int(input("Enter task index: "))
            
        mark_task_as_completed(task_index)

    elif action == "unmark":
        print_tasks()
        task_index = int(input("Enter task index: "))   
        while task_index >maxi:
            print("Index is out of range, please enter the looking available in the tasks")
            task_index = int(input("Enter task index: "))

        mark_task_as_not_completed(task_index)

    elif action == "delete":
        # fix what happens if the index is out of range
        task_index = int(input("Enter task index: "))
        while task_index >maxi:
            print("Index is out of range, please enter the looking available in the tasks")
            task_index = int(input("Enter task index: "))

        delete_task(task_index)

    elif action == "edit":
        task_index = int(input("Enter task index: "))
        while task_index >maxi:
            print("Index is out of range, please enter the looking available in the tasks")
            task_index = int(input("Enter task index: "))
        new_description = input("Enter new task description: ")
        edit_task(task_index, new_description)
    elif action == "quit":
        break
    else:
        print("Invalid action")
