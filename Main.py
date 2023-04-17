from tkinter import *
from SpFunc import *

root = Tk()

root.geometry('1200x600')
root.title('TRUSS ANALYSIS')
root.configure(bg='#b3bec2')
root.iconbitmap('favicon.ico')

frame = LabelFrame(root, text='BUTTON', padx=10, pady=5, bg='white', height=600, width=200,
                   relief=FLAT, fg='black')
frame.grid(column=0, row=0)
frame.grid_propagate(False)

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
properties_frame = LabelFrame(root, text='PROPERTIES', padx=5, pady=5, bg='#643c6a', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))

node_frame = LabelFrame(root, text='NODE PARAMETER', padx=5, pady=5, bg='#167288', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))

element_frame = LabelFrame(root, text='PROPERTIES', padx=5, pady=5, bg='#3cb464', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))

support_frame = LabelFrame(root, text='NODE PARAMETER', padx=5, pady=5, bg='#f6993f', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))

load_frame = LabelFrame(root, text='PROPERTIES', padx=5, pady=5, bg='#f66d9b', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))

solve_frame = LabelFrame(root, text='NODE PARAMETER', padx=5, pady=5, bg='#2c8160', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
##------------------------------------------------------------------------------------------------------------------------##


##----------------------------------------------- Default frame onscreen -------------------------------------------------##

properties_frame.grid(column=1, row=0)
properties_frame.grid_propagate(False)

Main_properties_frame = create_scrollbar_frame(properties_frame, 570, 380, '#643c6a')

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

analysis_frame_list = [properties_frame, node_frame, element_frame, support_frame, load_frame, solve_frame]

##------------------------------------------------------------------------------------------------------------------------##


##------------------------------------------------- Support Function -----------------------------------------------------##

def track_and_destroy(name):
    frame_id = frame_name_list.index(name)
    target = analysis_frame_list[frame_id]
    destroy_all(target)

##------------------------------------------------------------------------------------------------------------------------##


##------------------------------------- Information panel control function -----------------------------------------------##

def onscreen_now(keyword):
    global properties_frame
    global node_frame
    global element_frame
    global support_frame
    global load_frame
    global solve_frame
    global onscreen_frame
    global Frame_width
    global Frame_height

    track_and_destroy(onscreen_frame)
    

    if keyword == "properties_frame":
        
        properties_frame = LabelFrame(root, text='PROPERTIES', padx=5, pady=5, bg='#643c6a', height=Frame_height, width=Frame_width,
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
        onscreen_frame = "properties_frame"

    elif keyword == "node_frame":

        Node_entry_width = 15
        Node_entry_font = ('regular', 15)
        Node_label_font = ('regular', 10)
        Node_label_height = 2

        node_frame = LabelFrame(root, text='NODE PARAMETER', padx=5, pady=5, bg='#167288', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
        node_frame.grid(column=1, row=0)
        node_frame.grid_propagate(False)

        Main_node_frame = create_scrollbar_frame(node_frame, 570, 380, '#167288')

        Node_info_panel = Label(Main_node_frame, text="Enter number of nodes :", height=Node_label_height, width=20, font=Node_label_font, bg="#49B265", fg="white")
        Node_info_panel.grid(column=0, row=0, pady=10, padx=4, columnspan=3)

        NumberOfNode_Entry = Entry(Main_node_frame, width=Node_entry_width, font=Node_entry_font)
        NumberOfNode_Entry.grid(column=4, row=0, padx=4, pady=10, ipady=4, columnspan=3)

        def create_coor_info_entry(Data_entry):

            # print(type(Data_entry.get()))
            try:
                NumberOfEntry = int(Data_entry.get())
            except:
                print("Invalid data !!!")
            # print(NumberOfEntry)
            # print(type(NumberOfEntry))

            X_label = Label(Main_node_frame, text="X Coordinate", height=Node_label_height, width=10, font=Node_label_font, bg="#49B265", fg="white")
            Y_label = Label(Main_node_frame, text="Y Coordinate", height=Node_label_height, width=10, font=Node_label_font, bg="#49B265", fg="white")
            X_label.grid(column=2, row=2, padx=4, pady=10, columnspan=2)
            Y_label.grid(column=4, row=2, padx=4, pady=10, columnspan=2)    

            for entry in range(NumberOfEntry):
                Node_Label_children = Label(Main_node_frame, text="Node number " + str(entry) + " :", height=Node_label_height, width=15, font=Node_label_font, bg="#49B265", fg="white")
                Node_Label_children.grid(column=0, row=entry+3, padx=4, pady=3, columnspan=2)
                Node_X_coor_entry = Entry(Main_node_frame, width=15, font=Node_label_font)
                Node_X_coor_entry.grid(column=2, row=entry+3, padx=4, pady=3, columnspan=2, ipady=5)
                Node_Y_coor_entry = Entry(Main_node_frame, width=15, font=Node_label_font)
                Node_Y_coor_entry.grid(column=4, row=entry+3, padx=4, pady=3, columnspan=2, ipady=5)
            

        
        Okay_button = Button(Main_node_frame, width=43, height=2, text="OKAY !!!", bg="#FFD75F", fg="white", font=('regular',10), command=lambda: create_coor_info_entry(NumberOfNode_Entry))
        Okay_button.grid(column=0, row=1, columnspan=6, padx=5, pady=10)

        Update_properties_button = Button(Main_node_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
        # Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        onscreen_frame = "node_frame"
    
    elif keyword == "element_frame":

        element_frame = LabelFrame(root, text='ELEMENT PARAMETER', padx=5, pady=5, bg='#3cb464', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
        element_frame.grid(column=1, row=0)
        element_frame.grid_propagate(False)

        Main_element_frame = create_scrollbar_frame(element_frame, Frame_height - 30, Frame_width, '#3cb464')

        Update_properties_button = Button(Main_element_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
        Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        onscreen_frame = "element_frame"
    
    elif keyword == "support_frame":

        support_frame = LabelFrame(root, text='SUPPORT PARAMETER', padx=5, pady=5, bg='#f6993f', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
        support_frame.grid(column=1, row=0)
        support_frame.grid_propagate(False)

        Main_support_frame = create_scrollbar_frame(support_frame, Frame_height - 30, Frame_width, '#f6993f')

        Update_properties_button = Button(Main_support_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
        Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        onscreen_frame = "support_frame"
    
    elif keyword == "load_frame":

        load_frame = LabelFrame(root, text='LOAD PARAMETER', padx=5, pady=5, bg='#f66d9b', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
        load_frame.grid(column=1, row=0)
        load_frame.grid_propagate(False)

        Main_load_frame = create_scrollbar_frame(load_frame, Frame_height - 30, Frame_width, '#f66d9b')

        Update_properties_button = Button(Main_load_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
        Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        onscreen_frame = "load_frame"
    

    elif keyword == "solve_frame":

        solve_frame = LabelFrame(root, text='SOLVE', padx=5, pady=5, bg='#2c8160', height=Frame_height, width=Frame_width,
                   relief=FLAT, fg='white', font=('regular', font_size))
        solve_frame.grid(column=1, row=0)
        solve_frame.grid_propagate(False)

        Main_solve_frame = create_scrollbar_frame(solve_frame, Frame_height - 30, Frame_width, '#2c8160')

        Update_properties_button = Button(Main_solve_frame, width=15, height=2, text="UPDATE !!!", bg="#49B265", fg="white", font=('regular', 10))
        Update_properties_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        onscreen_frame = "solve_frame"
    
##------------------------------------------------------------------------------------------------------------------------##


##------------------------------------------------------------------------------------------------------------------------##

properties_button = Button(frame, text='PROPERTIES', height=button_height, width=button_width, bg='#643c6a', 
                           fg='#FFFFFF', relief=RAISED, font=('regular', font_size), command=lambda:onscreen_now("properties_frame"))
properties_button.grid(column=0, row=0, pady=10)

node_button = Button(frame, text='NODE', height=button_height, width=button_width, bg='#167288', fg='#FFFFFF', 
                     relief=RAISED, font=('regular', font_size), command=lambda:onscreen_now("node_frame"))
node_button.grid(column=0, row=1, pady=10)

element_button = Button(frame, text='ELEMENT', height=button_height, width=button_width, bg='#3cb464', 
                        fg='#FFFFFF', relief=RAISED, font=('regular', font_size), command=lambda:onscreen_now("element_frame"))
element_button.grid(column=0, row=2, pady=10)

support_button = Button(frame, text='SUPPORT', height=button_height, width=button_width, bg='#f6993f', 
                        fg='#FFFFFF', relief=RAISED, font=('regular', font_size), command=lambda:onscreen_now("support_frame"))
support_button.grid(column=0, row=3, pady=10)

load_button = Button(frame, text='LOAD', height=button_height, width=button_width, bg='#f66d9b', 
                     fg='#FFFFFF', relief=RAISED, font=('regular', font_size), command=lambda:onscreen_now("load_frame"))
load_button.grid(column=0, row=4, pady=10)

solve_button = Button(frame, text='SOLVE', height=button_height, width=button_width, bg='#2c8160', 
                     fg='#FFFFFF', relief=RAISED, font=('regular', font_size), command=lambda:onscreen_now("solve_frame"))
solve_button.grid(column=0, row=5, pady=10)

exit_button = Button(frame, text='EXIT', height=button_height, width=button_width, bg='#b45248', 
                     fg='#FFFFFF', relief=RAISED, font=('regular', font_size), command=root.destroy)
exit_button.grid(column=0, row=6, pady=10)



root.mainloop()