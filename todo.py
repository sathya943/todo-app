# todo.py
import sys
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

tasks = load_tasks()

def add_task(task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Task removed: {removed}")
    else:
        print("❌ Invalid task number!")

def show_tasks():
    if not tasks:
        print("📋 No tasks yet! Add some tasks.")
    else:
        print("\n📋 === YOUR TODO LIST ===")
        print(f"Total tasks: {len(tasks)}")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("=======================")

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
                print("❌ Please provide a valid number")
        else:
            print("Usage: python todo.py [add|list|remove] [text/number]")
    else:
        show_tasks()