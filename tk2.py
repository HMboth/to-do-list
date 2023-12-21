from tkinter import *

#******************FUNCTIONS************************************
def add():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

def delete():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        pass

def delete_all():
    listbox.delete(0, END)
#******************FUNCTIONS************************************
#******************WIDGETS************************************
root = Tk()
root.geometry("550x350")
root.title("To-Do List")

title = Label(root, text="To-Do List", fg="blue", font=("Times", "24", "bold italic"))
title.place(y=20, x=200)

label = Label(root, text="Enter the Task:", font=("Times", "10","bold italic"))
label.place(x=150, y=80)
entry = Entry(root, font=("Times","10"))
entry.place(x=250, y=80)
#*******************BUTTONS************************************

addbtn = Button(root, text="Add Task", width=15, bg="blue",fg="white", font=("Times", "10","bold italic"),command=add)
addbtn.place(x=400, y=150)

deletebtn = Button(root, text="Delete Task", width=15,bg="blue",fg="white", font=("Times", "10","bold italic"), command=delete)
deletebtn.place(x=400, y=205)

delete_allbtn = Button(root, text="Delete All", width=15,bg="blue",fg="white", font=("Times", "10","bold italic"), command=delete_all)
delete_allbtn.place(x=400, y=255)

exitbtn = Button(root, text="Exit", width=15,bg="blue",fg="white", font=("Times", "10","bold italic"), command=root.quit)
exitbtn.place(x=400, y=305)
#*******************BUTTONS************************************
label2 = Label(root, text="Tasks : ", font=("Times", "15","bold italic"))
label2.place(x=50, y=120)
listbox = Listbox(root, width=50, height=11, font=("Times","10"))
listbox.place(x=50, y=150)


root.mainloop()
