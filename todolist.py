##########################         Importing all the necessary modules
from tkinter import *

##########################        Initializing the GUI
root = Tk()
root.title('WELCOME TO PYTHON PROGRAMMING')
root.geometry('1100x500')
root.config(bg="khaki")

#########################         Heading Label

Label(root, text='Anjali Samshete To-Do List', bg='skyblue', font=("castellar", 25,'bold'), wraplength=1100).place(x=600, y=0)

####################              Listbox with all the tasks with a Scrollbar
tasks = Listbox(root, selectbackground='black', bg='pink', font=('Helvetica', 22), height=20, width=5)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=1180, y=50, height=742)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=305, y=50)


###########################        Creating the Entry widget
new_item_entry = Entry(root, width=49, font=('bold',14))
new_item_entry.place(x=460, y=720)

############################        Buttons
add_btn = Button(root, text='Add Item', bg='green', width=10, font=('Helvetica', 14),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=460, y=745)

delete_btn = Button(root, text='Delete Item', bg='green', width=10, font=('Helvetica', 14),
                 command=lambda: delete_item(tasks))
delete_btn.place(x=884, y=745)


##############################       Adding and Deleting
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open('tasks.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')


def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)


##########################           Finalizing
root.update()
root.mainloop()