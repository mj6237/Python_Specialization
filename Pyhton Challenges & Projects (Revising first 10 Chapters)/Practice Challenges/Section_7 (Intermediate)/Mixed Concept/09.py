'''
1. Initialize an empty list todo_list = []. 
2. Define a function add_task(task_list, task_description) that adds a task_description to 
task_list and prints a confirmation. 
3. Define a function view_tasks(task_list) that prints all tasks with their numbers (e.g., "1. Buy groceries"). 
If the list is empty, print "No tasks in the list." 
4. Use a while True loop for a menu: 
 1. Add Task 
 2. View Tasks 
 3. Exit 
5. Call the appropriate function based on user choice. Use try-except ValueError for menu input. 
'''
todo_list = []

def add_task(task_list, task_description):
    task_list.append(task_description)
    print(f"Task '{task_description}' added successfully!")

def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(task_list):
            print(f"{i + 1}. {task}")
        print("-----------------------")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("-----------------------")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task_desc = input("Enter task description: ")
            add_task(todo_list, task_desc)
        elif choice == 2:
            view_tasks(todo_list)
        elif choice == 3:
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number corresponding to the menu option.")
