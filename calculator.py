import tkinter as tk
from tkinter import messagebox
def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)
root = tk.Tk()
root.title("Calculator 🐻")
root.geometry("300x400")
root.configure(bg="#8bdce8")
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief=tk.GROOVE)
entry.pack(fill="both", padx=10, pady=10)
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]
emoji_map = {
    "+": "➕", "-": "➖", "×": "✖", "÷": "➗", "=": "=", "C": "🗑"
}
for row in buttons:
    frame = tk.Frame(root, bg="#8bdce8")
    frame.pack(fill="both", expand=True)
    for btn in row:
        text = emoji_map.get(btn, btn)
        button = tk.Button(
            frame, text=text, font=("Arial", 18), bg="white", fg="black", 
            relief=tk.RAISED, padx=10, pady=10,
            command=lambda b=btn: on_click(b)
        )
        button.pack(side="left", fill="both", expand=True, padx=5, pady=5)
root.mainloop()
