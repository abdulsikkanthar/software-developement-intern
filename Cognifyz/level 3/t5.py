class Task:
    def __init__(self, task_id, description, status):
        self.task_id = task_id
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task_id, description, status = line.strip().split(",")
                    self.tasks.append(Task(task_id, description, status))
        except FileNotFoundError:
            print("No tasks file found. Starting with an empty task list.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    file.write(f"{task.task_id},{task.description},{task.status}\n")
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def create_task(self, task_id, description, status):
        task = Task(task_id, description, status)
        self.tasks.append(task)
        self.save_tasks()

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"ID: {task.task_id}, Description: {task.description}, Status: {task.status}")

    def update_task(self, task_id, new_description, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = new_description
                task.status = new_status
                self.save_tasks()
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return
        print("Task not found.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter task ID: ")
            description = input("Enter task description: ")
            status = input("Enter task status: ")
            task_manager.create_task(task_id, description, status)
        elif choice == "2":
            task_manager.read_tasks()
        elif choice == "3":
            task_id = input("Enter task ID to update: ")
            new_description = input("Enter new description: ")
            new_status = input("Enter new status: ")
            task_manager.update_task(task_id, new_description, new_status)
        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            task_manager.delete_task(task_id)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
