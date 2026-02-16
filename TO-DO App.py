import json
import os
FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(" Task added!")
ef view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    idx = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("Task Completed!")
