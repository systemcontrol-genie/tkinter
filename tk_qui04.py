import tkinter as tk

import serial



def Cbutton(master, text, color, side, text_color, command=None):
    button = tk.Button(master, text=text, bg=color, fg=text_color, width=10, height=3, command= command)
    button.pack(side=side, padx=10, pady=10)

def send_command(command):
    ser.write(command.enable())
def turn_on_red():
    send_command("R")
def turn_on_green():
    send_command("G")
def turn_on_blue():
    send_command("B")
def turn_on_Yollow():
    send_command("Y")
def turn_on_stop():
    send_command("S")
def Offbutton():
    pass
window = tk.Tk()
ser = serial.Serial("COM5", 9600, timeout=1)
window.geometry("400x400")
window.title('Color Buttons')

Cbutton(window, '빨강', 'red', 'left', 'white', command = turn_on_red)
Cbutton(window, '노랑', 'yellow', 'right', 'black',command = turn_on_Yollow)
Cbutton(window, '초록', 'green', 'top', 'white', command = turn_on_green)
Cbutton(window, '파랑', 'blue', 'bottom', 'white', command = turn_on_blue)

offButton = tk.Button(window, text="꺼짐", command = Offbutton, bg="white", fg='black', width=10, height=3)
offButton.place(relx=0.5,rely=0.5, anchor="center")

window.mainloop()