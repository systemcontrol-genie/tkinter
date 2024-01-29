from tkinter import *
def clicking():
    

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.title("Spinbox")

sp =Spinbox(win)
sp.config(from_=-1, to =3)
sp.pack()

btn = Button(win)
btn.config(text = "선택")
btn.config(command=clicking)

lab = Label(win)
lab.pack()

win.mainloop()
