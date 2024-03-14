class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task_index):
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed successfully!")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No tasks to display.")

def main():
    todo_list = TodoList()

    while True:
        print("\n===== TODO LIST MENU =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            if todo_list.tasks:
                task_index = int(input("Enter task index to remove: ")) - 1
                todo_list.remove_task(task_index)
            else:
                print("No tasks to remove.")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
