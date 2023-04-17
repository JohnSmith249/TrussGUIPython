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
        for widget in frame.winfo_children():
            widget.destroy()
        frame.destroy()
    except:
        print("No onscreen frame to destroy !!!")
    