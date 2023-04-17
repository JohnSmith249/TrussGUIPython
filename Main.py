from tkinter import *
from SpFunc import *
from tkinter import ttk

root = Tk()

root.geometry('1200x650')
root.title('TRUSS ANALYSIS')
root.configure(bg='#b3bec2')
root.iconbitmap('favicon.ico')

working_tab = ttk.Notebook(root)
working_tab.grid(column=0, row=0)
# frame = LabelFrame(root, text='BUTTON', padx=10, pady=5, bg='white', height=600, width=200,
#                    relief=FLAT, fg='black')
# frame.grid(column=0, row=0)
# frame.grid_propagate(False)

button_height = 2
button_width = 18
font_size = 12

label_height = 2
label_witdth = 15
label_font_size = 10

entry_width = 21
entry_font_size = 10

Frame_width = 380
Frame_height = 600

frame_name_list = ["properties_frame", "node_frame", "element_frame", "support_frame", "load_frame", "solve_frame"]
onscreen_frame = "properties_frame"


##------------------------------------------------Frame-------------------------------------------------------------------##

properties_frame = LabelFrame(working_tab, text='PROPERTIES', padx=5, pady=5, bg='#643c6a', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
properties_frame.grid(column=1, row=0)
properties_frame.grid_propagate(False)

Main_properties_frame = create_scrollbar_frame(properties_frame, Frame_height - 30, Frame_width, '#643c6a')

Unit_label = Label(Main_properties_frame, text="Unit (U)", height=label_height, width=label_witdth, bg='#49B265', fg='white', font=('regular', label_font_size))
Area_label = Label(Main_properties_frame, text="Area (A)", height=label_height, width=label_witdth, bg='#49B265', fg='white', font=('regular', label_font_size))
Young_modulus_lable = Label(Main_properties_frame, text="Young Modulus (E)", height=label_height, width=label_witdth, bg='#49B265', fg='white', font=('regular', label_font_size))

Unit_label.grid(column=0, row=0, pady=10, padx=5)
Area_label.grid(column=0, row=1, pady=10, padx=5)
Young_modulus_lable.grid(column=0, row=2, pady=10, padx=5)


Unit_entry = Entry(Main_properties_frame, width=entry_width, font=('regular', entry_font_size))
Area_entry = Entry(Main_properties_frame, width=entry_width, font=('regular', entry_font_size))
Young_modulus_entry = Entry(Main_properties_frame, width=entry_width, font=('regular', entry_font_size))

Unit_entry.grid(column=1, row=0, padx=15, ipady=5)
Area_entry.grid(column=1, row=1, ipady=5)
Young_modulus_entry.grid(column=1, row=2, ipady=5)

Update_properties_button = Button(Main_properties_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

node_frame = LabelFrame(working_tab, text='NODE PARAMETER', padx=5, pady=5, bg='#167288', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
Node_entry_width = 15
Node_entry_font = ('regular', 15)
Node_label_font = ('regular', 10)
Node_label_height = 2

node_frame.grid(column=1, row=0)
node_frame.grid_propagate(False)

Main_node_frame = create_scrollbar_frame(node_frame, 570, 310, '#167288')

Node_info_panel = Label(Main_node_frame, text="Enter number of nodes :", height=Node_label_height, width=20, font=Node_label_font, bg="#49B265", fg="white")
Node_info_panel.grid(column=0, row=0, pady=10, padx=4, columnspan=3)

NumberOfNode_Entry = Entry(Main_node_frame, width=Node_entry_width, font=Node_entry_font)
NumberOfNode_Entry.grid(column=3, row=0, padx=4, pady=10, ipady=4, columnspan=3) 

Okay_button = Button(Main_node_frame, width=43, height=2, text="OKAY !!!", bg="#FFD75F", fg="white", font=('regular',10), command=lambda: create_coor_info_entry(NumberOfNode_Entry, Main_node_frame))
Okay_button.grid(column=0, row=1, columnspan=6, padx=5, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

element_frame = LabelFrame(working_tab, text='PROPERTIES', padx=5, pady=5, bg='#3cb464', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
element_frame.grid(column=1, row=0)
element_frame.grid_propagate(False)

Main_element_frame = create_scrollbar_frame(element_frame, Frame_height - 30, Frame_width, '#3cb464')

Update_properties_button = Button(Main_element_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

support_frame = LabelFrame(working_tab, text='NODE PARAMETER', padx=5, pady=5, bg='#f6993f', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
support_frame.grid(column=1, row=0)
support_frame.grid_propagate(False)

Main_support_frame = create_scrollbar_frame(support_frame, Frame_height - 30, Frame_width, '#f6993f')

Update_properties_button = Button(Main_support_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

load_frame = LabelFrame(working_tab, text='PROPERTIES', padx=5, pady=5, bg='#f66d9b', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
load_frame.grid(column=1, row=0)
load_frame.grid_propagate(False)

Main_load_frame = create_scrollbar_frame(load_frame, Frame_height - 30, Frame_width, '#f66d9b')

Update_properties_button = Button(Main_load_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

solve_frame = LabelFrame(working_tab, text='NODE PARAMETER', padx=5, pady=5, bg='#2c8160', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
solve_frame.grid(column=1, row=0)
solve_frame.grid_propagate(False)

Main_solve_frame = create_scrollbar_frame(solve_frame, Frame_height - 30, Frame_width, '#2c8160')

Update_properties_button = Button(Main_solve_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

##------------------------------------------------------------------------------------------------------------------------##


##------------------------------------------------------------------------------------------------------------------------##

working_tab.add(properties_frame, text="Properties")
working_tab.add(node_frame, text="Node Info")
working_tab.add(element_frame, text="Element Info")
working_tab.add(support_frame, text="Support Info")
working_tab.add(load_frame, text="Load Info")
working_tab.add(solve_frame, text="Solve Info")

##------------------------------------------------------------------------------------------------------------------------##

##------------------------------------------------- Support Function -----------------------------------------------------##
def name_of_active_widget():
    global root
    for widget in root.winfo_children:
        print(widget)
        print("*"*50)
        print(type(widget))
        print("*"*50)
##------------------------------------------------------------------------------------------------------------------------##

root.mainloop()