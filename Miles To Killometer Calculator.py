import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

#functions
def convert():
    mile_input = entry_int.get()
    km_output = round(mile_input * 1.60934,3)
    output_string.set(km_output)

def change_theme():
    cuurrent_style = style.theme.name
    if cuurrent_style=="journal":
        style.theme_use("darkly")
    else:
        style.theme_use("journal")

#window

# window = tk.Tk()
window = ttk.Window(title="Miles to Kilometers",size=(500,300))
# window.title("Miles to Kilometers") #for set title of window
# window.geometry("300x150") #widthxheight
# window.iconbitmap("logo.ico")
style = ttk.Style("journal")

#title
#font="font fontsize style"
title_label = ttk.Label(master=window,text="Miles to Kilometers" ,font="Calibri 24 bold") 
title_label.pack()

#input field
input_frame = ttk.Frame(master=window,)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame,textvariable=entry_int)
button = ttk.Button(master=input_frame , text= "Convert" ,command=convert)
entry.pack(side="left",padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,text="OUTPUT" , font="Calibri 24",textvariable=output_string)
output_label.pack(pady=5)

#for change theme button
theme_button = ttk.Button(master=window,text="Change Theme",command=change_theme)
theme_button.pack()

#run
window.mainloop()