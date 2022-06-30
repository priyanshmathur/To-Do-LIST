from copyreg import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root  = Tk()
root.geometry("500x500")

#Define our font
my_font = Font(
    family="Gabriola",
    size = 30,
    weight = "bold"
)

#create frame
my_frame = Frame(root)
my_frame.pack(pady = 10)

#Create a list box
my_list = Listbox(my_frame,
    font = my_font,
    width = 25,
    height = 5,
    bg = "SystemButtonFace",
    bd = 0,
    fg = "#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none",

)

my_list.pack(side = LEFT , fill = BOTH)

#Create dummy list
stuff = ["Walk the Dog" , "Buy Groceries" , "Call mom" , "Rule the World"]
#Add dummy list to list box
for item in stuff:
    my_list.insert(END,item)

#Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side = RIGHT , fill = BOTH)

#Add scroll bar
my_list.config(yscrollcommand = my_scrollbar.set)
my_scrollbar.config(command = my_list.yview)

#Create an entry box to add items to the list
my_entry = Entry(root , font = ("Helvetica" , 24), width =26)
my_entry.pack(pady = 20)

#Create a button frame
button_frame = Frame(root)
button_frame.pack(pady = 20)

#FUNCTIONS
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)

def cross_off_item():
    #Cross o item
    my_list.itemconfig(
        my_list.curselection(),
        fg = "#dedede"
    )
    #get rid of selection bar
    my_list.selection_clear(0,END)

def uncross_item():
     #Cross o item
    my_list.itemconfig(
        my_list.curselection(),
        fg = "#464646"
    )
    #get rid of selection bar
    my_list.selection_clear(0,END)

def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count+=1

def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:\python_lab\TS101\To - Do List Python\data",
        title="Save File",
        filetypes=(
            ("Dat Files","*.dat"),
            ("All Files","*.*")
            )
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        #Delete crossed off items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count+=1
        
        #lets grab all the stuff from the list
        stuff = my_list.get(0,END)

        #open the file
        output_file = open(file_name,'wb')

        #Actually add the stuff to the file
        pickle.dump(stuff,output_file)



def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:\python_lab\TS101\To - Do List Python\data",
        title="Open File",
        filetypes=(
            ("Dat Files","*.dat"),
            ("All Files","*.*")
            )
    )

    if file_name:
        #Delete currently opened list
        my_list.delete(0,END)

        #Open the file
        input_file = open(file_name,'rb')

        #load the data from the file
        stuff = pickle.load(input_file)

        #output stuff to screen
        for item in stuff:
            my_list.insert(END, item)


def delete_list():
    my_list.delete(0,END)
#Create Menu
my_menu = Menu(root)
root.config(menu = my_menu)

#Add items to the menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File" , menu=file_menu)

#Add drop down items
file_menu.add_command(label = "Save List", command = save_list)
file_menu.add_command(label = "Open List", command = open_list)
file_menu.add_separator()
file_menu.add_command(label = "Delete List", command = delete_list)


#Add some buttons
delete_button = Button(button_frame , text = "Delete Item" , command = delete_item)
add_button = Button(button_frame , text = "Add Item" , command = add_item)
cross_off_button = Button(button_frame , text = "Cross-Off Item" , command = cross_off_item)
uncross_button = Button(button_frame , text = "Uncross Item" , command = uncross_item)
delete_cross_button  = Button(button_frame , text = "Delete crossed Item" , command = delete_crossed)

delete_button.grid(row = 0 , column = 0)
add_button.grid(row = 0 , column = 1, padx = 20)
cross_off_button.grid(row = 0 , column = 2)
uncross_button.grid(row = 0 , column = 3, padx = 20)
delete_cross_button.grid(row = 0 , column = 4)



root.mainloop()