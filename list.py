import tkinter as tk
import json
import os

if os.path.exists("todo.json"):
    with open("todo.json", "r") as f:
        tasks = json.load(f)
else:
    tasks = []
def save():
    with open("todo.json", "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
        save()

root = tk.Tk()
root.title("Simple To-Do")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

for t in tasks:
    listbox.insert(tk.END, t)

root.mainloop()
