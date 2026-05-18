# todo.py
import sys

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✅ Task added: {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️  Task removed: {removed}")
    else:
        print("Invalid task number!")

def show_tasks():
    '''Displays the list of tasks with their corresponding numbers.'''
    if not tasks:
        print("No tasks in the list!")
    else:
        print("📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "add" and len(sys.argv) > 2:
            add_task(" ".join(sys.argv[2:]))
        elif sys.argv[1] == "list":
            show_tasks()
        elif sys.argv[1] == "remove" and len(sys.argv) > 2:
            try:
                remove_task(int(sys.argv[2]) - 1)
            except:
                print("Please provide a valid number")
    else:
        show_tasks()