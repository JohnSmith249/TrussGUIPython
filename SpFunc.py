from tkinter import *
from tkinter import ttk
import math
from truss import Result, init_truss, plot_diagram

def write_result(data, mode):
    try:
        write_file = open("result.txt", mode)
        write_file.write(data)
        write_file.close()
    except:
        print("Write ERROR !!!")


def create_scrollbar_frame(main_frame, H, W, Bg):
    # Create A Canvas
    my_canvas = Canvas(main_frame, height=H, width=W, bg=Bg)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # Create another frame inside the canvas
    second_frame = Frame(my_canvas, bg=Bg)

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    return second_frame


def destroy_all(frame):
    try:
        for widget in frame.winfo_children():
            widget.destroy()
        # frame.destroy()
        # print(frame.winfo_children())
        # print(len(frame.winfo_children()))
    except:
        print("No onscreen frame to destroy !!!")


def destroy_all_widget(frame, keep_list, widget_list):
    try:
        for widget in widget_list:
            if widget not in keep_list:
                widget.destroy()
        # children_widget[-1].destroy()
    except:
        print("No widget to destroy ")


def process_data(raw_data, mode):
    if mode == 2:
        Info = []
        Value = []
        for i in range(len(raw_data)):
            if i%2 == 0:
                Info.append(raw_data[i])
            else:
                Value.append(raw_data[i])
        print(Info)
        print(Value)
        return Info, Value

    if mode == 3:
        Info=[]
        Value1 = []
        Value2 = []
        for i in range(len(raw_data)):
            try:
                Info.append(raw_data[0])
                raw_data.pop(0)
                Value1.append(raw_data[0])
                raw_data.pop(0)
                Value2.append(raw_data[0])
                raw_data.pop(0)
            except:
                print("End of data")
                break
        print(Info)
        print(Value1)
        print(Value2)
        return Info, Value1, Value2

def get_data(frame):
    raw_data = []
    for widget in frame.winfo_children():
        if widget.winfo_class() == 'Entry':
            raw_data.append[widget.get()]
            print(widget.get())
    return raw_data

def process_data_and_solve():
    with open('Properties_data.txt','r') as data_file:
        data = data_file.readlines()
        Unit_sys = (data[2].split(':')[1]).replace(' ','')
        Area = int((data[3].split(':')[1]).replace(' ',''))
        Young_modulus = (data[4].split(':')[1]).replace(' ','')
        Young_data = Young_modulus.split('e')
        Young_modulus = int(Young_data[0]) * (10**int(Young_data[1]))

    with open('Node_data.txt','r') as data_file:
        coordinate = []
        data = data_file.readlines()
        data.remove(data[0])
        data.remove(data[0])
        for i in data:
            node_number = int(i.split(' '*22)[0].split('node')[1])
            x_coordinate = float(i.split(' '*22)[1])
            y_coordinate = float(i.split(' '*22)[2])
            coordinate.append((x_coordinate, y_coordinate))
    # print(coordinate)

    corespond_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open('Element_data.txt','r') as data_file:
        element = []
        data = data_file.readlines()
        data.remove(data[0])
        data.remove(data[0])
        for i in data:
            node_number = int(i.split(' '*19)[0].split('element')[1])
            begin_node = int(i.split(' '*19)[1]) - 1
            end_node = int(i.split(' '*19)[2]) - 1
            element_bar = corespond_letter[begin_node] + corespond_letter[end_node]
            element.append(element_bar)
    # print(element)

    with open('support_data.txt','r') as data_file:
        support = []
        corespond_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        data = data_file.readlines()
        data.remove(data[0])
        data.remove(data[0])
        for i in data:
            node_number = int(i.split(' '*19)[0].split('node')[1]) - 1 
            supported_node = corespond_letter[node_number]
            support_type = str(i.split(' '*22)[1][0])
            if support_type == 'P':
                support_command = 'pin'
                support.append((supported_node, support_command))
            elif support_type == 'V':
                support_command = 'roller'
                angle = math.pi/2
                support.append((supported_node, support_command, angle))
            elif support_type == 'H':
                support_command = 'roller'
                angle = 0
                support.append((supported_node, support_command, angle))
        
        # print(support)


    with open('Load_data.txt','r') as data_file:
        load = []
        corespond_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        data = data_file.readlines()
        data.remove(data[0])
        data.remove(data[0])
        for i in data:
            node_number = int(i.split(' '*16)[0].split('node')[1]) - 1
            loaded_node = corespond_letter[node_number]
            Force_X = float(i.split(' '*16)[1])
            Force_Y = float(i.split(' '*16)[2])
            load.append((loaded_node, Force_X, Force_Y))

    my_truss = init_truss('My first truss')
    my_truss.add_joints(coordinate)
    my_truss.add_bars(element)
    my_truss.add_loads(load)
    my_truss.add_supports(support)
    my_truss.solve_and_plot()
    results = Result(my_truss)
    print(results)