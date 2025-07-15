import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌈 Mini Task Manager")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f8ff")  # Light pastel background

        self.tasks = load_tasks()

        # Title Label
        self.title = tk.Label(root, text="Mini Task Manager", font=("Segoe UI", 18, "bold"), bg="#f0f8ff", fg="#333")
        self.title.pack(pady=10)

        # Entry + Add Button Frame
        self.input_frame = tk.Frame(root, bg="#f0f8ff")
        self.input_frame.pack(pady=5)

        self.entry = tk.Entry(self.input_frame, width=28, font=("Segoe UI", 12))
        self.entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(self.input_frame, text="➕ Add", bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"),
                                    activebackground="#45a049", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        # Listbox
        self.listbox = tk.Listbox(root, width=40, height=10, font=("Segoe UI", 11), bg="#ffffff", fg="#000080",
                                  selectbackground="#87CEFA", activestyle="none")
        self.listbox.pack(pady=15)

        # Delete Button
        self.delete_button = tk.Button(root, text="❌ Delete Selected Task", bg="#e91e63", fg="white",
                                       font=("Segoe UI", 10, "bold"), activebackground="#c2185b",
                                       command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_to_listbox()

    def load_to_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.save_and_reload()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("⚠️ Empty Task", "Please enter a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.save_and_reload()
        else:
            messagebox.showinfo("ℹ️ No Selection", "Please select a task to delete.")

    def save_and_reload(self):
        save_tasks(self.tasks)
        self.load_to_listbox()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
