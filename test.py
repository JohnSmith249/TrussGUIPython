# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title('Test Notebook')
# root.geometry("500x500")

# my_notebook = ttk.Notebook(root)
# my_notebook.pack(pady=15)

# my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
# my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

# my_frame1.pack(fill="both", expand=1)
# my_frame2.pack(fill="both", expand=1)
# my_notebook.add(my_frame1, text="Blue Tab")
# my_notebook.add(my_frame2, text="red tab")

# root.mainloop()

# from test_complete_examples import *
from truss import Result, init_truss, plot_diagram
import math

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
            # print(widget.get())
    return raw_data

# raw_data = [1,'P',3,'V',5,'P',7,'H']
# data = process_data(raw_data, 2)
# node_number = data[0]
# type_of_support = data[1]
# with open('support_data.txt', 'w+') as data_file:
#     text = "Load"
#     label_text = ' '*10 + "node number" + ' '*10 + "type of support" + ' '*10 + "\n"
#     data_file.write(text)
#     data_file.write("\n")
#     data_file.write(label_text)
#     for i in range(len(node_number)):
#         data_text = ' '*10 + "node " + str(node_number[i]) + ' '*22 + str(type_of_support[i]) + ' '*10 + "\n"
#         data_file.write(data_text)
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

# print(load)

my_truss = init_truss('My first truss')
my_truss.add_joints([(0, 0), (290, -90), (815, 127.5), (290, 345), (0, 255), (220.836, 127.5)])
my_truss.add_bars(['AB', 'BC', 'CD', 'DE', 'EF', 'AF', 'DF', 'BF'])
my_truss.add_loads([('C', 0, -0.675)])
my_truss.add_supports([('A', 'roller', math.pi/2), ('E', 'pin'), ('B', 'roller', -math.pi/2)])
my_truss.solve_and_plot()
results = Result(my_truss)
print(results)