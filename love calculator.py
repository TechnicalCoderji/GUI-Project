import tkinter as tk
import ttkbootstrap as ttk

#functions
def get_love_percentage():
    love_percentage = 0
    first_name = entry_name_1.get()
    second_name = entry_name_2.get()

    if first_name and second_name:
        love_list = []
        for c in first_name + second_name:
            love_list.append(ord(c))
        
        love_percentage = sum(love_list) % 100

    else:
        love_percentage = "Invalid Name"

    if love_percentage <= 20:
        love_percentage = f"😢😢 {love_percentage}% 😢😢"
    elif love_percentage <= 40:
        love_percentage = f"😊😊 {love_percentage}% 😊😊"
    elif love_percentage <= 60:
        love_percentage = f"😍😍 {love_percentage}% 😍😍"
    elif love_percentage <= 80:
        love_percentage = f"💖💖 {love_percentage}% 💖💖"
    else:
        love_percentage = f"💗💗💗 {love_percentage}% 💗💗💗"

    output_string.set(love_percentage)

#window

# window = tk.Tk()
window = ttk.Window(title="Love Calculator",size=(500,300))
window.iconbitmap("logo.ico")
style = ttk.Style("darkly")

#title
#font="font fontsize style"
title_label = ttk.Label(master=window,text="Love Calculator" ,font="Calibri 24 bold") 
title_label.pack()

#input field
label_frame = ttk.Frame(master=window)
first_name_label = ttk.Label(master=label_frame,text="Boy Name", font = "Calibri 15")
second_name_label = ttk.Label(master=label_frame,text="Girl Name", font = "Calibri 15")

first_name_label.pack(side="left",padx=30)
second_name_label.pack(side="left",padx=60)
label_frame.pack()

input_frame = ttk.Frame(master=window)

entry_name_1 = tk.StringVar()
entry_name_2 = tk.StringVar()

entry_1 = ttk.Entry(master=input_frame,textvariable=entry_name_1)
entry_2 = ttk.Entry(master=input_frame,textvariable=entry_name_2)

entry_1.pack(side="left",padx=10)
entry_2.pack(side="left",padx=10)
input_frame.pack(pady=10)

button = ttk.Button(master=window , text= "Convert" ,command=get_love_percentage)
button.pack()

#output
output_string = tk.StringVar(value="💗💗💗99%💗💗💗")
output_label = ttk.Label(master=window,text="OUTPUT" , font="Calibri 24",textvariable=output_string)
output_label.pack(pady=5)

#run
window.mainloop()