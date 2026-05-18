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
    if not tasks:
        print("📋 No tasks yet! Add some tasks.")

    else:
        print("\n📋 === YOUR TODO LIST ===")
        for i, task in enumerate(tasks, 1):

            print(f"{i}. {task}")
        print("=======================")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"🗑️  Task deleted: {task}")
    else:
        print("Task not found!")
def clear_all_tasks():
    global tasks
    tasks = []
    print("All tasks cleared!")
    # TODO: Add confirmation

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
        
print("This is a simple change.")Change 1
Change 2
