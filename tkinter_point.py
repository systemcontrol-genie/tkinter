from tkinter import *

win = Tk()
win.geometry("700x500")
win.title("test")
win.option_add("*Font", "맑은고딕 20")

x_, y_ =20, 30
btn1 = Button(win)
btn1.config(text = f"{x_},{y_}")
btn1.place(x=x_,y=y_)
btn1.pack()
btn2 = Button(win)
rel_x, rel_y = 0.1, 0.1
btn2.config(text = f"{rel_x},{rel_y}")
btn2.place(rel_x=rel_x , rel_y=rel_y)
btn2.pack()


win.mainloop()
