import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# สร้างหน้าต่าง
root = tk.Tk()
root.title("To Do List")

# สร้างอิลิเมนต์
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
entry = tk.Entry(root)
add_button = tk.Button(root, text="เพิ่ม", command=add_task)
delete_button = tk.Button(root, text="ลบ", command=delete_task)

# แสดงอิลิเมนต์บนหน้าต่าง
listbox.pack()
entry.pack()
add_button.pack()
delete_button.pack()

# เริ่มการรันแอปพลิเคชัน
root.mainloop()