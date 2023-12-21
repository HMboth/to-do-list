from tkinter import *
#*****************FUNCTIONS****************************
def add():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

def remove():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

#*****************FUNCTIONS****************************
#*****************WIDGETS****************************
root = Tk()
root.config(bg="pink")
root.geometry("400x400")
root.title("To-Do List")

title = Label(root, text="TO-DO LIST", fg="purple", bg="pink",font=("Times", "24", "bold italic"))
title.pack(pady=10)

label = Label(root, text="Enter Task :", bg="pink",fg="white",font=("Times", "12", "bold"))
label.pack()
entry = Entry(root, width=40,font=("Times", "10"))
entry.pack(pady=10)

add_button = Button(root, text="Add Task",bg="purple", fg="white", width=20,font=("Times", "10", "bold") ,command=add)
add_button.pack(pady=5)

listbox = Listbox(root, selectmode=SINGLE, width=60, height=10,font=("Times", "10"))
listbox.pack(pady=10)

remove_button = Button(root, text="Remove Task",bg="purple", fg="white", width=20,font=("Times", "10", "bold") , command=remove)
remove_button.pack(pady=5)

root.mainloop()
