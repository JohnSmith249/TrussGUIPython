from tkinter import *
from tkinter import ttk

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
        for widget in frame.grid_slaves():
            widget.destroy()
        frame.destroy()
    except:
        print("No onscreen frame to destroy !!!")


def destroy_all_widget(frame):
    try:
        for widget in frame.grid_slaves():
            widget.destroy()
    except:
        print("No widget to destroy ")


def create_coor_info_entry(Data_entry, main_frame):

    keep_widget = [".!labelframe8.!canvas.!frame.!label",
                   ".!labelframe8.!canvas.!frame.!entry",
                   ".!labelframe8.!canvas.!frame.!button",
                   ".!labelframe8.!canvas.!frame.!button2"]
    
    for widget in main_frame.winfo_children():
            widget.destroy()
    print("******************************************************************************")
    
    try:
        NumberOfEntry = int(Data_entry.get())
        destroy_all_widget(main_frame)
    except:
        print("Invalid data !!!")   

    Node_label_font = ('regular', 10)
    Node_label_height = 2

    X_label = Label(main_frame, text="X Coordinate", height=Node_label_height, width=10, font=Node_label_font, bg="#49B265", fg="white")
    Y_label = Label(main_frame, text="Y Coordinate", height=Node_label_height, width=10, font=Node_label_font, bg="#49B265", fg="white")
    X_label.grid(column=2, row=2, padx=4, pady=10, columnspan=2)
    Y_label.grid(column=4, row=2, padx=4, pady=10, columnspan=2)    

    for entry in range(NumberOfEntry):
        Node_Label_children = Label(main_frame, text="Node number " + str(entry) + " :", height=Node_label_height, width=15, font=Node_label_font, bg="#49B265", fg="white")
        Node_Label_children.grid(column=0, row=entry+3, padx=4, pady=3, columnspan=2)
        Node_X_coor_entry = Entry(main_frame, width=15, font=Node_label_font)
        Node_X_coor_entry.grid(column=2, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
        Node_Y_coor_entry = Entry(main_frame, width=15, font=Node_label_font)
        Node_Y_coor_entry.grid(column=4, row=entry+3, padx=4, pady=3, columnspan=2, ipady=6)
    Update_properties_button = Button(main_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10), command=lambda: destroy_all_widget(main_frame))
    Update_properties_button.grid(column=0, row=NumberOfEntry+3, columnspan=6, padx=10, pady=10)