# todo.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Build a Todo App")
    show_tasks()