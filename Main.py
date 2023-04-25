from tkinter import *
from SpFunc import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from anastruct import SystemElements
from SolveEngine01 import SolveEngine01, Read_data
from SolveEngine02 import Solve_Engine_02
import os

root = Tk()

root.geometry('1300x670')
root.title('TRUSS ANALYSIS')
root.configure(bg='#b3bec2')
root.iconbitmap('favicon.ico')

working_tab = ttk.Notebook(root)
working_tab.grid(column=0, row=0)

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

# coordinates_test_data = [(0, 0), (290, -90), (815, 127.5), (290, 345), (0, 255), (220.836, 127.5)]
fig = Figure(figsize=(8,6), dpi=100)
# ax = fig.add_subplot()
# ax.set_xlabel("X axis")
# ax.set_ylabel("Y axis")
# ax.set_title("Element vizualization")
# ax.plot(coordinates_test_data[0][0], coordinates_test_data[0][1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
canvas = FigureCanvasTkAgg(fig, root)
# toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
# toolbar.update()

canvas.get_tk_widget().grid(column=2, row=0, padx=5, pady=10)
# toolbar.grid(column=2, row=0)

##------------------------------------------------Frame-------------------------------------------------------------------##

properties_frame = LabelFrame(working_tab, text='PROPERTIES', padx=5, pady=5, bg='#643c6a', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
properties_frame.grid(column=1, row=0, rowspan=2)
properties_frame.grid_propagate(False)

# properties_frame = create_scrollbar_frame(properties_frame, Frame_height - 30, Frame_width, '#643c6a')

Unit_label = Label(properties_frame, text="Unit (U)", height=label_height, width=label_witdth, bg='#49B265', fg='white', font=('regular', label_font_size))
Area_label = Label(properties_frame, text="Area (A)", height=label_height, width=label_witdth, bg='#49B265', fg='white', font=('regular', label_font_size))
Young_modulus_lable = Label(properties_frame, text="Young Modulus (E)", height=label_height, width=label_witdth, bg='#49B265', fg='white', font=('regular', label_font_size))

Unit_label.grid(column=0, row=0, pady=10, padx=5)
Area_label.grid(column=0, row=1, pady=10, padx=5)
Young_modulus_lable.grid(column=0, row=2, pady=10, padx=5)

Unit_option_list = ["mm, N, Pa, kg", "in, N, psi, lb"]
Unit_value = StringVar(root)
Unit_value.set("Chose Unit system")

Unit_menu = OptionMenu(properties_frame, Unit_value, *Unit_option_list)
Unit_menu.config(width=entry_width, font=('regular', entry_font_size))

Area_entry = Entry(properties_frame, width=entry_width, font=('regular', entry_font_size))
Young_modulus_entry = Entry(properties_frame, width=entry_width, font=('regular', entry_font_size))

Unit_menu.grid(column=1, row=0, padx=15, ipady=5)
Area_entry.grid(column=1, row=1, ipady=5, padx=15)
Young_modulus_entry.grid(column=1, row=2, ipady=5, padx=15)

Node_data = Read_data("nodes")
Properties_data = Read_data("properties")
Element_data = Read_data("elements")
Support_data = Read_data("supports")
Load_data = Read_data("loads")

A = Properties_data[0]
E = Properties_data[1]

def record_properties_data():

    global Unit_value
    global Area_entry
    global Young_modulus_entry

    with open('Properties_data.txt','w') as data_file:
        data_file.write("Properties Data \n")
        data_file.write("\n")
        data_file.write("*"*50)
        data_file.write("   - Unit System: " + str(Unit_value.get()) + "\n")
        data_file.write("   - Area Value : " + str(Area_entry.get()) + "\n")
        data_file.write("   - Young modulus: " + str(Young_modulus_entry.get()) + "\n")
        data_file.write("*"*50)

Update_properties_button = Button(properties_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10), command=record_properties_data)
Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

node_frame = LabelFrame(working_tab, text='NODE PARAMETER', padx=5, pady=5, bg='#167288', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))

Node_entry_width = 15
Node_entry_font = ('regular', 15)
Node_label_font = ('regular', 10)
Node_label_height = 2

def open_result():
    os.startfile("Full_result.txt")
    os.startfile("Result_log.txt")

def Solve_and_show():
    After_solve_frame = Frame(root, padx=5, pady=5, bg='#3d5a80', height=600, width=800,
                   relief=FLAT)
    After_solve_frame.grid(column=2, row=0, padx=5, pady=10)
    Figures = Solve_Engine_02('graph')
    Result_show_tab = ttk.Notebook(After_solve_frame)
    Result_show_tab.pack(padx=5, pady=5)

    structure = Frame(Result_show_tab, height=600, width=800, bg='#90eebf')
    axial_force = Frame(Result_show_tab, height=600, width=800, bg='#90eebf')
    bending_moment = Frame(Result_show_tab, height=600, width=800, bg='#90eebf')
    shear_force = Frame(Result_show_tab, height=600, width=800, bg='#90eebf')
    displacement = Frame(Result_show_tab, height=600, width=800, bg='#90eebf')

    structure.pack(fill="both", expand=1)
    axial_force.pack(fill="both", expand=1)
    # bending_moment.pack(fill="both", expand=1)
    # shear_force.pack(fill="both", expand=1)
    displacement.pack(fill="both", expand=1)

    Frames = [structure, axial_force, displacement]
    Frames_name = ["structure", "axial_force", "displacement"]

    Result_show_tab.add(structure, text="STRUCTURE")
    Result_show_tab.add(axial_force, text="AXIAL FORCE")
    # Result_show_tab.add(bending_moment, text="BENDING MOMENT")
    # Result_show_tab.add(shear_force, text="SHEAR FORCE")
    Result_show_tab.add(displacement, text="DISPLACMENT")

    global canvas

    for i in range(len(Figures)):
        try:
            canvas.get_tk_widget().grid_forget()
        except:
            pass
        print(Figures[i])
        canvas = FigureCanvasTkAgg(Figures[i], Frames[i])
        canvas.get_tk_widget().pack(fill="both", expand=1)

def record_data(frame, mode):
    raw_data = []
    for widget in frame.winfo_children():
        if widget.winfo_class() == 'Entry':
            raw_data.append(widget.get())
    print(raw_data)
    global canvas

    if mode == 'node':
        data = process_data(raw_data, 2)
        x_coor = data[0]
        y_coor = data[1]
        # print(x_coor)
        # print(y_coor)
        with open('Node_data.txt', 'w+') as data_file:
            text = "Node Coordinate data"
            label_text = ' '*10 + "node number" + ' '*10 + "X coordinate" + ' '*10 + "Y coordinate" + "\n"
            data_file.write(text)
            data_file.write("\n")
            data_file.write(label_text)
            for i in range(len(x_coor)):
                data_text = ' '*10 + "node " + str(i) + ' '*22 + str(x_coor[i]) + ' '*22 + str(y_coor[i]) + "\n"
                data_file.write(data_text)

    elif mode == 'load':
        data = process_data(raw_data, 3)
        node_number = data[0]
        force_X = data[1]
        force_Y = data[2]
        with open('Load_data.txt', 'w+') as data_file:
            text = "Load data"
            label_text = ' '*10 + "node number" + ' '*10 + "X Force" + ' '*10 + "Y Force" + "\n"
            data_file.write(text)
            data_file.write("\n")
            data_file.write(label_text)
            for i in range(len(node_number)):
                data_text = ' '*10 + "node " + str(node_number[i]) + ' '*18 + str(force_X[i]) + ' '*16 + str(force_Y[i]) + "\n"
                data_file.write(data_text)
        
        ss = SystemElements(EA=E*A, figsize=(8,6))
        for i in range(len(Element_data)):
            begin = Element_data[i][0]
            end = Element_data[i][1]
            begin_coor = list(Node_data[begin])
            end_coor = list(Node_data[end])
            ss.add_truss_element(location=[begin_coor, end_coor])
        
        for i in range(len(Load_data)):
            node_index = Load_data[i][0] + 1
            Force_x = Load_data[i][1]
            Force_y = Load_data[i][2]
            ss.point_load(node_id=node_index, Fx=Force_x, Fy=Force_y)
        fig = ss.show_structure(show=False)
        
        try:
            canvas.get_tk_widget().grid_forget()
        except:
            pass
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(column=2, row=0, padx=5, pady=10)

    elif mode == 'support':
        data = process_data(raw_data, 2)
        node_number = data[0]
        type_of_support = data[1]
        with open('support_data.txt', 'w+') as data_file:
            text = "Support data"
            label_text = ' '*10 + "node number" + ' '*10 + "type of support" + "\n"
            data_file.write(text)
            data_file.write("\n")
            data_file.write(label_text)
            for i in range(len(node_number)):
                data_text = ' '*10 + "node " + str(node_number[i]) + ' '*22 + str(type_of_support[i]) + "\n"
                data_file.write(data_text)
        ss = SystemElements(EA=E*A, figsize=(8,6))
        for i in range(len(Element_data)):
            begin = Element_data[i][0]
            end = Element_data[i][1]
            begin_coor = list(Node_data[begin])
            end_coor = list(Node_data[end])
            ss.add_truss_element(location=[begin_coor, end_coor])
        for i in range(len(Support_data)):
            node_index = Support_data[i][0] + 1
            support_type = Support_data[i][1]
            if support_type == 'P':
                ss.add_support_hinged(node_id=node_index)
            if support_type == 'V':
                ss.add_support_roll(node_id=node_index, direction=2)
            if support_type == 'H':
                ss.add_support_roll(node_id=node_index, direction=1)
        fig = ss.show_structure(show=False)
        # global canvas
        try:
            canvas.get_tk_widget().grid_forget()
        except:
            pass
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(column=2, row=0, padx=5, pady=10)
    
    elif mode == 'element':
        data = process_data(raw_data, 2)
        begin_node = data[0]
        end_node = data[1]
        with open('Element_data.txt', 'w+') as data_file:
            text = "Element data"
            label_text = ' '*10 + "element number" + ' '*10 + "begin node" + ' '*10 + "end node" + "\n"
            data_file.write(text)
            data_file.write("\n")
            data_file.write(label_text)
            for i in range(len(begin_node)):
                data_text = ' '*10 + "element " + str(i) + ' '*19 + str(begin_node[i]) + ' '*19 + str(end_node[i]) + "\n"
                data_file.write(data_text)
        ss = SystemElements(EA=E*A, figsize=(8,6))
        for i in range(len(Element_data)):
            begin = Element_data[i][0]
            end = Element_data[i][1]
            begin_coor = list(Node_data[begin])
            end_coor = list(Node_data[end])
            ss.add_truss_element(location=[begin_coor, end_coor])
        # Show update on structure plot
        fig = ss.show_structure(show=False)
        # global canvas
        try:
            canvas.get_tk_widget().grid_forget()
        except:
            pass
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(column=2, row=0, padx=5, pady=10)


def create_coor_info_entry():

    global NumberOfNode_Entry
    global node_frame

    try:
        NumberOfEntry = int(NumberOfNode_Entry.get())
        # destroy_all(main_frame)
    except:
        print("Invalid data !!!")   


    my_canvas = Canvas(node_frame, height=570, width=380, bg='#167288')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(node_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # Create another frame inside the canvas
    main_frame = Frame(my_canvas, bg='#167288')

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0,0), window=main_frame, anchor="nw")

    Node_label_font = ('regular', 10)
    Node_label_height = 2
    
    X_label = Label(main_frame, text="X Coordinate", height=Node_label_height, width=10, font=Node_label_font, bg="#49B265", fg="white")
    Y_label = Label(main_frame, text="Y Coordinate", height=Node_label_height, width=10, font=Node_label_font, bg="#49B265", fg="white")
    X_label.grid(column=2, row=2, padx=4, pady=10, columnspan=2)
    Y_label.grid(column=4, row=2, padx=4, pady=10, columnspan=2)    

    for entry in range(1, NumberOfEntry+1):
        Node_Label_children = Label(main_frame, text="Node number " + str(entry) + " :", height=Node_label_height, width=15, font=Node_label_font, bg="#49B265", fg="white")
        Node_Label_children.grid(column=0, row=entry+3, padx=4, pady=3, columnspan=2)
        Node_X_coor_entry = Entry(main_frame, width=15, font=Node_label_font)
        Node_X_coor_entry.grid(column=2, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
        Node_Y_coor_entry = Entry(main_frame, width=15, font=Node_label_font)
        Node_Y_coor_entry.grid(column=4, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
    Update_properties_button = Button(main_frame, width=15, height=2, text="UPDATE !!!", bg='#df2525', fg="white", font=('regular', 10), command=lambda:record_data(main_frame,'node'))
    Update_properties_button.grid(column=0, row=NumberOfEntry+4, columnspan=6, padx=10, pady=10)

NumberOfNode_Entry = Entry(node_frame, width=Node_entry_width, font=Node_entry_font)
NumberOfNode_Entry.grid(column=3, row=0, padx=4, pady=10, ipady=4, columnspan=3)

node_frame.grid(column=1, row=0, rowspan=2)
node_frame.grid_propagate(False)

Node_info_panel = Label(node_frame, text="Enter number of nodes :", height=Node_label_height, width=20, font=Node_label_font, bg="#49B265", fg="white")
Node_info_panel.grid(column=0, row=0, pady=10, padx=4, columnspan=3)

Okay_button = Button(node_frame, width=43, height=2, text="OKAY !!!", bg='#df2525', fg="white", font=('regular',10), command=create_coor_info_entry)
Okay_button.grid(column=0, row=1, columnspan=6, padx=5, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

element_frame = LabelFrame(working_tab, text='ELEMENT INFO', padx=5, pady=5, bg='#3cb464', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
element_frame.grid(column=1, row=0)
element_frame.grid_propagate(False)

Element_entry_width = 15
Element_entry_font = ('regular', 15)
Element_label_font = ('regular', 10)
Element_label_height = 2

def create_element_info_entry():

    global NumberOfElement_Entry
    global element_frame

    try:
        NumberOfEntry = int(NumberOfElement_Entry.get())
    except:
        print("Invalid data !!!")   

    my_canvas = Canvas(element_frame, height=570, width=380, bg='#3cb464')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(element_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # Create another frame inside the canvas
    main_frame = Frame(my_canvas, bg='#3cb464')

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0,0), window=main_frame, anchor="nw")

    Element_label_font = ('regular', 10)
    Element_label_height = 2
    
    begin_label = Label(main_frame, text="Begin Node", height=Element_label_height, width=10, font=Element_label_font, bg='#167288', fg="white")
    end_label = Label(main_frame, text="End Node", height=Element_label_height, width=10, font=Element_label_font, bg='#167288', fg="white")
    begin_label.grid(column=2, row=2, padx=4, pady=10, columnspan=2)
    end_label.grid(column=4, row=2, padx=4, pady=10, columnspan=2)    

    for entry in range(1, NumberOfEntry+1):
        Element_Label_children = Label(main_frame, text="Element number " + str(entry) + " :", height=Element_label_height, width=15, font=Element_label_font, bg='#167288', fg="white")
        Element_Label_children.grid(column=0, row=entry+3, padx=4, pady=3, columnspan=2)
        Node_X_coor_entry = Entry(main_frame, width=15, font=Element_label_font)
        Node_X_coor_entry.grid(column=2, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
        Node_Y_coor_entry = Entry(main_frame, width=15, font=Element_label_font)
        Node_Y_coor_entry.grid(column=4, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
    Update_properties_button = Button(main_frame, width=15, height=2, text="UPDATE !!!", bg='#df2525', fg="white", font=('regular', 10), command=lambda:record_data(main_frame,'element'))
    Update_properties_button.grid(column=0, row=NumberOfEntry+4, columnspan=6, padx=10, pady=10)

NumberOfElement_Entry = Entry(element_frame, width=Element_entry_width, font=Element_entry_font)
NumberOfElement_Entry.grid(column=3, row=0, padx=4, pady=10, ipady=4, columnspan=3)

element_frame.grid(column=1, row=0, rowspan=2)
element_frame.grid_propagate(False)

Node_info_panel = Label(element_frame, text="Enter number of nodes :", height=Element_label_height, width=20, font=Element_label_font, bg='#167288', fg="white")
Node_info_panel.grid(column=0, row=0, pady=10, padx=4, columnspan=3)

Okay_button = Button(element_frame, width=43, height=2, text="OKAY !!!", bg='#df2525', fg="white", font=('regular',10), command=create_element_info_entry)
Okay_button.grid(column=0, row=1, columnspan=6, padx=5, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

support_frame = LabelFrame(working_tab, text='SUPPORT INFO', padx=5, pady=5, bg='#f6993f', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
support_frame.grid(column=1, row=0)
support_frame.grid_propagate(False)

Support_entry_width = 15
Support_entry_font = ('regular', 15)
Support_label_font = ('regular', 10)
Support_label_height = 2

def create_Support_info_entry():

    global NumberOfSupport_Entry
    global Support_frame

    try:
        NumberOfEntry = int(NumberOfSupport_Entry.get())
        # destroy_all(main_frame)
    except:
        print("Invalid data !!!")   

    my_canvas = Canvas(support_frame, height=570, width=380, bg='#3cb464')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(support_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # Create another frame inside the canvas
    main_frame = Frame(my_canvas, bg='#3cb464')

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0,0), window=main_frame, anchor="nw")

    Support_label_font = ('regular', 10)
    Support_label_height = 2
    
    node_support_label = Label(main_frame, text="Supported Node", height=Support_label_height, width=12, font=Support_label_font, bg='#167288', fg="white")
    type_of_support_label = Label(main_frame, text="Type of Support", height=Support_label_height, width=15, font=Support_label_font, bg='#167288', fg="white")
    node_support_label.grid(column=2, row=2, padx=4, pady=10, columnspan=2)
    type_of_support_label.grid(column=4, row=2, padx=4, pady=10, columnspan=2)    

    for entry in range(1, NumberOfEntry+1):
        Support_Label_children = Label(main_frame, text="Support number " + str(entry) + " :", height=Support_label_height, width=15, font=Support_label_font, bg='#167288', fg="white")
        Support_Label_children.grid(column=0, row=entry+3, padx=4, pady=3, columnspan=2)
        Node_X_coor_entry = Entry(main_frame, width=15, font=Support_label_font)
        Node_X_coor_entry.grid(column=2, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
        Node_Y_coor_entry = Entry(main_frame, width=15, font=Support_label_font)
        Node_Y_coor_entry.grid(column=4, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
    Update_properties_button = Button(main_frame, width=15, height=2, text="UPDATE !!!", bg='#df2525', fg="white", font=('regular', 10), command=lambda:record_data(main_frame,'support'))
    Update_properties_button.grid(column=0, row=NumberOfEntry+4, columnspan=6, padx=10, pady=10)

NumberOfSupport_Entry = Entry(support_frame, width=Support_entry_width, font=Support_entry_font)
NumberOfSupport_Entry.grid(column=3, row=0, padx=4, pady=10, ipady=4, columnspan=3)

support_frame.grid(column=1, row=0, rowspan=2)
support_frame.grid_propagate(False)

Node_info_panel = Label(support_frame, text="Enter number of nodes :", height=Support_label_height, width=20, font=Support_label_font, bg='#167288', fg="white")
Node_info_panel.grid(column=0, row=0, pady=10, padx=4, columnspan=3)

Okay_button = Button(support_frame, width=43, height=2, text="OKAY !!!", bg='#df2525', fg="white", font=('regular',10), command=create_Support_info_entry)
Okay_button.grid(column=0, row=1, columnspan=6, padx=5, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

Load_frame = LabelFrame(working_tab, text='LOAD INFO', padx=5, pady=5, bg='#af7c74', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
Load_frame.grid(column=1, row=0)
Load_frame.grid_propagate(False)

Load_entry_width = 15
Load_entry_font = ('regular', 15)
Load_label_font = ('regular', 10)
Load_label_height = 2

def create_Load_info_entry():

    global NumberOfLoad_Entry
    global Load_frame

    try:
        NumberOfEntry = int(NumberOfLoad_Entry.get())
    except:
        print("Invalid data !!!")   

    my_canvas = Canvas(Load_frame, height=570, width=380, bg='#af7c74')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(Load_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # Create another frame inside the canvas
    main_frame = Frame(my_canvas, bg='#af7c74')

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0,0), window=main_frame, anchor="nw")

    Load_label_font = ('regular', 10)
    Load_label_height = 2
    
    Node_applied_load_label = Label(main_frame, text="Loaded Node", height=Load_label_height, width=12, font=Load_label_font, bg='#167288', fg="white")
    force_in_horizontal = Label(main_frame, text="Horizontal Force", height=Load_label_height, width=15, font=Load_label_font, bg='#167288', fg="white")
    force_in_vertical = Label(main_frame, text="Vertical Force", height=Load_label_height, width=15, font=Load_label_font, bg='#167288', fg="white")
    Node_applied_load_label.grid(column=0, row=2, padx=4, pady=10, columnspan=2)
    force_in_horizontal.grid(column=2, row=2, padx=4, pady=10, columnspan=2)
    force_in_vertical.grid(column=4, row=2, padx=4, pady=10, columnspan=2)    

    for entry in range(1, NumberOfEntry+1):
        Node_applied_load = Entry(main_frame, width=15, font=Load_label_font)
        Node_applied_load.grid(column=0, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
        Froce_in_X = Entry(main_frame, width=15, font=Load_label_font)
        Froce_in_X.grid(column=2, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
        Froce_in_Y = Entry(main_frame, width=15, font=Load_label_font)
        Froce_in_Y.grid(column=4, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
    Update_properties_button = Button(main_frame, width=15, height=2, text="UPDATE !!!", bg='#df2525', fg="white", font=('regular', 10), command=lambda:record_data(main_frame,'load'))
    Update_properties_button.grid(column=0, row=NumberOfEntry+4, columnspan=6, padx=10, pady=10)

NumberOfLoad_Entry = Entry(Load_frame, width=7, font=Load_entry_font)
NumberOfLoad_Entry.grid(column=3, row=0, padx=4, pady=10, ipady=4, columnspan=3)

Load_frame.grid(column=1, row=0, rowspan=2)
Load_frame.grid_propagate(False)

Node_info_panel = Label(Load_frame, text="Enter number of apply load nodes :", height=Load_label_height, width=25, font=Load_label_font, bg='#167288', fg="white")
Node_info_panel.grid(column=0, row=0, pady=10, padx=4, columnspan=3)

Okay_button = Button(Load_frame, width=43, height=2, text="OKAY !!!", bg='#df2525', fg="white", font=('regular',10), command=create_Load_info_entry)
Okay_button.grid(column=0, row=1, columnspan=6, padx=5, pady=10)

##------------------------------------------------Frame-------------------------------------------------------------------##

solve_frame = LabelFrame(working_tab, text='NODE PARAMETER', padx=5, pady=5, bg='#3d5a80', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
solve_frame.grid(column=1, row=0, rowspan=2)
solve_frame.grid_propagate(False)

Solve_button = Button(solve_frame, text="SOLVE !!!", height=4, width=25, bg='#2c8160', fg="white", command=Solve_and_show, font=('regular', 15))
Solve_button.pack(fill="none", expand=True)

Export_button = Button(solve_frame, text="SHOW RESULT !!!", height=4, width=25, bg='#569DAA', fg="white", command=open_result, font=('regular', 15))
Export_button.pack(fill="none", expand=True)

Exit_button = Button(solve_frame, text="EXIT !!!", height=4, width=25, bg='#df2525', fg="white", command=root.destroy, font=('regular', 15))
Exit_button.pack(fill="none", expand=True)
##------------------------------------------------------------------------------------------------------------------------##


##------------------------------------------------------------------------------------------------------------------------##

working_tab.add(properties_frame, text="Properties")
working_tab.add(node_frame, text="Node Info")
working_tab.add(element_frame, text="Element Info")
working_tab.add(support_frame, text="Support Info")
working_tab.add(Load_frame, text="Load Info")
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