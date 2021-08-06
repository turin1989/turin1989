from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import font

joints = 6
joint_list = []

for i in range(0, int(joints)):
    joint_list.append(i)
    i += 1
    
def donothing():
    filewin = Toplevel(master)
    button = Button(filewin, text="Do nothing button")
    button.pack()
   
def arm_wizard():
    wiz = Toplevel(master, height="600", width="300")
    start_button = Button(wiz, text="Start")
    start_button.grid(row = 0, column = 0)
    
def close():
    exit()
    
def load_config():
    filename = askopenfilename()

readout_font = ("OCR A Extended", 20, "bold")

master = Tk()
master.title("Valkyrie Robotics")
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Config", command=donothing)
filemenu.add_command(label="Load Config", command=load_config)
filemenu.add_command(label="Save Config", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=close)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Joint Wizard", command=arm_wizard)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

master.config(menu=menubar)

#Initialize row/column configuration
master.rowconfigure(0, minsize = 800, weight = 1, pad = 5)
master.rowconfigure(1, minsize = 200, weight = 1, pad = 5)
master.columnconfigure([0, 1, 2], minsize = 400, weight = 1, pad = 5)

#Initialize frames
fr_joint_positions = tk.Frame(master, bg="black")
fr_joint_positions.rowconfigure(joint_list, weight = 1, pad = 5)
fr_joint_positions.columnconfigure([0, 1], weight = 1, pad = 5)

fr_effector_position = tk.Frame(master, bg="black")
fr_effector_position.rowconfigure(joint_list, weight = 1, pad = 5)
fr_effector_position.columnconfigure([0, 1, 2], weight = 1, pad = 5)

fr_macros = tk.Frame(master, bg="black")
fr_macros.rowconfigure([0, 1, 2], weight = 1, pad = 5)
fr_macros.columnconfigure([0, 1, 2], weight = 1, pad = 5)

fr_animate = tk.Frame(master, bg="gray")
fr_speed = tk.Frame(master, bg="black")
fr_mode = tk.Frame(master, bg="black")
fr_mode.rowconfigure([0, 1, 2, 3], weight = 1, pad = 5)
fr_mode.columnconfigure([0, 1, 2], weight = 1, pad = 5)

#Initialize labels
lbl_effector_position = tk.Label(master, text = "Effector Position", bg="black", fg="green")
lbl_pos_x = tk.Label(fr_effector_position, text = "0.000", bg="black", fg="green")
lbl_pos_x.config(font=("OCR A Extended", 24))
lbl_pos_x_axis = tk.Label(fr_effector_position, text = "x:", bg="black", fg="green")
lbl_pos_x_axis.config(font=("OCR A Extended", 12))
lbl_pos_y = tk.Label(fr_effector_position, text = "0.000", bg="black", fg="green")
lbl_pos_y.config(font=("OCR A Extended", 24))
lbl_pos_y_axis = tk.Label(fr_effector_position, text = "y:", bg="black", fg="green")
lbl_pos_y_axis.config(font=("OCR A Extended", 12))
lbl_pos_z = tk.Label(fr_effector_position, text = "0.000", bg="black", fg="green")
lbl_pos_z.config(font=("OCR A Extended", 24))
lbl_pos_z_axis = tk.Label(fr_effector_position, text = "z:", bg="black", fg="green")
lbl_pos_z_axis.config(font=("OCR A Extended", 12))
lbl_pos_a = tk.Label(fr_effector_position, text = "0.000", bg="black", fg="green")
lbl_pos_a.config(font=("OCR A Extended", 24))
lbl_pos_a_axis = tk.Label(fr_effector_position, text = "a:", bg="black", fg="green")
lbl_pos_a_axis.config(font=("OCR A Extended", 12))
lbl_pos_b = tk.Label(fr_effector_position, text = "0.000", bg="black", fg="green")
lbl_pos_b.config(font=("OCR A Extended", 24))
lbl_pos_b_axis = tk.Label(fr_effector_position, text = "b:", bg="black", fg="green")
lbl_pos_b_axis.config(font=("OCR A Extended", 12))
lbl_pos_c = tk.Label(fr_effector_position, text = "0.000", bg="black", fg="green")
lbl_pos_c.config(font=("OCR A Extended", 24))
lbl_pos_c_axis = tk.Label(fr_effector_position, text = "c:", bg="black", fg="green")
lbl_pos_c_axis.config(font=("OCR A Extended", 12))

lbl_joint_positions = tk.Label(master, text = "Joint Positions", bg="black", fg="green")
lbl_macros = tk.Label(master, text = "Macros", bg="black", fg = "green")
lbl_animate = tk.Label(master, text = "Arm Position", bg="gray", fg = "green")
lbl_speed = tk.Label(master, text = "Jog Speed & Increments", bg="black", fg = "green")
lbl_mode = tk.Label(master, text = "Jog Mode", bg="black", fg = "green")


#Initialize buttons
btn_macro0 = tk.Button(fr_macros, text="Macro 0")
btn_macro1 = tk.Button(fr_macros, text="Macro 1")
btn_macro2 = tk.Button(fr_macros, text="Macro 2")
btn_macro3 = tk.Button(fr_macros, text="Macro 3")
btn_macro4 = tk.Button(fr_macros, text="Macro 4")
btn_macro5 = tk.Button(fr_macros, text="Macro 5")
btn_mode0 = tk.Checkbutton(fr_mode, text="Linear Move", bg = "black", fg = "green")
btn_mode1 = tk.Checkbutton(fr_mode, text="Circular Move", bg = "black", fg = "green")
btn_mode2 = tk.Checkbutton(fr_mode, text="Minimum Joint Movement", bg = "black", fg = "green")

#Initialize alphanumeric readouts
joints = [0, 1, 2, 3, 4, 5]
txt_joint0 = Text
    
    

#Place frames
fr_joint_positions.grid(row = 0, column = 0, sticky="nsew")
fr_effector_position.grid(row = 0, column = 1, sticky="nsew")
fr_macros.grid(row = 1, column = 2, sticky="nsew")
fr_animate.grid(row = 0, column = 2, sticky="nsew")
fr_speed.grid(row = 1, column = 0, sticky="nsew")
fr_mode.grid(row = 1, column = 1, sticky="nsew")

#Place labels
lbl_effector_position.grid(row = 0, column = 1, sticky = 'n')
lbl_pos_x.grid(row = 0, column = 1, sticky = 'nsew')
lbl_pos_x_axis.grid(row = 0, column = 0, sticky = 'e')
lbl_pos_y.grid(row = 1, column = 1, sticky = 'nsew')
lbl_pos_y_axis.grid(row = 1, column = 0, sticky = 'e')
lbl_pos_z.grid(row = 2, column = 1, sticky = 'nsew')
lbl_pos_z_axis.grid(row = 2, column = 0, sticky = 'e')
lbl_pos_a.grid(row = 3, column = 1, sticky = 'nsew')
lbl_pos_a_axis.grid(row = 3, column = 0, sticky = 'e')
lbl_pos_b.grid(row = 4, column = 1, sticky = 'nsew')
lbl_pos_b_axis.grid(row = 4, column = 0, sticky = 'e')
lbl_pos_c.grid(row = 5, column = 1, sticky = 'nsew')
lbl_pos_c_axis.grid(row = 5, column = 0, sticky = 'e')

lbl_joint_positions.grid(row = 0, column = 0, sticky = 'n')
lbl_macros.grid(row = 1, column = 2, sticky="n")
lbl_animate.grid(row = 0, column = 2, sticky="n")
lbl_speed.grid(row = 1, column = 0, sticky="n")
lbl_mode.grid(row = 1, column = 1, sticky="n")

#Place buttons
btn_macro0.grid(row = 1, column = 0)
btn_macro1.grid(row = 1, column = 1)
btn_macro2.grid(row = 1, column = 2)
btn_macro3.grid(row = 2, column = 0)
btn_macro4.grid(row = 2, column = 1)
btn_macro5.grid(row = 2, column = 2)
btn_mode0.grid(row = 1, column = 1, sticky="w")
btn_mode1.grid(row = 2, column = 1, sticky="w")
btn_mode2.grid(row = 3, column = 1, sticky="w")

master.mainloop()