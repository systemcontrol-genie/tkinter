#readio button 각각의 하나의 객체에 묶여 있어서 하나만 구성.

from tkinter import *


win =Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.title("Radio Button")

def clicking():
    a = rv.get()
    aa = a+1
    lab['text'] = aa

    

rv = IntVar()
rb1 = Radiobutton(win , text="#1", value=0, variable=rv)
rb2 = Radiobutton(win , text="#2", value=1, variable=rv)
rb3 = Radiobutton(win , text="#3", value=2, variable=rv)
rb1.pack()
rb2.pack()
rb3.pack()

btn = Button(win)
btn.config(text = "선택")
btn.config(command=clicking)
btn.pack()

lab =Label(win)
lab.pack()

win.mainloop()