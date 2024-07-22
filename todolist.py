# Function to display the menu options
def display_menu():
    print("\nSimple To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a task to the list
def add_task(task_list):
    task = input("Enter the task to add: ")
    task_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks(task_list):
    if not task_list:
        print("No tasks.")
    else:
        print("\nTasks:")
        for index, task in enumerate(task_list, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_completed(task_list):
    view_tasks(task_list)
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        task_list[task_index]["completed"] = True
        print(f"Task '{task_list[task_index]['task']}' marked as completed.")
    except IndexError:
        print("Invalid task number. Please try again.")

# Function to delete a task
def delete_task(task_list):
    view_tasks(task_list)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        task_deleted = task_list.pop(task_index)
        print(f"Task '{task_deleted['task']}' deleted.")
    except IndexError:
        print("Invalid task number. Please try again.")

# Main function to run the program
def main():
    task_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            mark_completed(task_list)
        elif choice == '4':
            delete_task(task_list)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
